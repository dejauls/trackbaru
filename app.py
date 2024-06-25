from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

client = MongoClient('mongodb://belajar:belajar@ac-pewhlve-shard-00-00.m1k88nt.mongodb.net:27017,ac-pewhlve-shard-00-01.m1k88nt.mongodb.net:27017,ac-pewhlve-shard-00-02.m1k88nt.mongodb.net:27017/?ssl=true&replicaSet=atlas-i3tctf-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
db = client.linkc

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('link.html')

@app.route("/link", methods=["POST"])
def link_post():
    try:
        platform = request.form['platform']
        print(f"Received platform: {platform}") 
        
        current_time = datetime.now().strftime('%Y-%m-%d')  
        doc = {
            'platform': platform,
            'timestamp': current_time  
        }

        result = db.link.insert_one(doc)
        print(f"Document inserted with id: {result.inserted_id}")  # Debug: Print insertion result

        return jsonify({'msg': 'POST request received!'})
    except Exception as e:
        print(f"Error: {e}")  # Debug: Print any error that occurs
        return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500

@app.route('/view_data', methods=['GET'])
def view_data():
    try:
        date = request.args.get('date')
        query = {}
        if date:
            query['timestamp'] = date
        
        data = list(db.link.find(query, {'_id': 0, 'platform': 1, 'timestamp': 1}))
        return render_template('data.html', data=data)
    except Exception as e:
        print(f"Error: {e}")  # Debug: Print any error that occurs
        return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500
    
@app.route('/data_today', methods=['GET'])
def data_today():
    try:
        today = datetime.today().strftime('%Y-%m-%d')
        data = list(db.link.find({'timestamp': today}, {'_id': 0, 'platform': 1, 'timestamp': 1}))
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500    
    
@app.route('/data_month', methods=['GET'])
def data_month():
    try:
        today = datetime.today()
        first_day_of_month = today.replace(day=1)
        data = list(db.link.find({'timestamp': {'$gte': first_day_of_month.strftime('%Y-%m-%d')}}, {'_id': 0, 'platform': 1, 'timestamp': 1}))
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500

@app.route('/data_week', methods=['GET'])
def data_week():
    try:
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        data = list(db.link.find({'timestamp': {'$gte': start_of_week.strftime('%Y-%m-%d')}}, {'_id': 0, 'platform': 1, 'timestamp': 1}))
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500    


# @app.route("/link", methods=["POST"])
# def link_post():
#     try:
#         instagram_receive = request.form['instagram_give']
#         print(f"Received data: {instagram_receive}") 
        
#         current_time = datetime.now().strftime('%Y-%m-%d')  
#         doc = {
#             'instagram': instagram_receive,
#             'timestamp': current_time  
#         }

#         result = db.link.insert_one(doc)
#         print(f"Document inserted with id: {result.inserted_id}")  # Debug: Print insertion result

#         return jsonify({'msg': 'POST request received!'})
#     except Exception as e:
#         print(f"Error: {e}")  # Debug: Print any error that occurs
#         return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500
    

# @app.route('/view_data', methods=['GET'])
# def view_data():
#     try:
#         date = request.args.get('date')
#         query = {}
#         if date:
#             query['timestamp'] = date
        
#         data = list(db.link.find(query, {'_id': 0, 'instagram': 1, 'timestamp': 1}))
#         return render_template('data.html', data=data)
#     except Exception as e:
#         print(f"Error: {e}")  # Debug: Print any error that occurs
#         return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500    

# @app.route('/view_data')
# def view_data():
#     try:
  
#         data = list(db.link.find({}, {'_id': 0, 'instagram': 1, 'timestamp': 1}))
#         return render_template('data.html', data=data)
#     except Exception as e:
#         print(f"Error: {e}")  
#         return jsonify({'msg': 'An error occurred', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# (tambah data)
# doc = {
#     'clik':'1',
#     # 'whatsapp':'1',
# }

# db.link.insert_one(doc)


# @app.route('/')
# def home():
#     return render_template('index.html')



# @app.route("/movie", methods=["POST"])
# def movie_post():
#     url_receive = request.form['url_give']
#     star_receive = request.form['star_give']
#     comment_receive = request.form['comment_give']


#     image = og_image['content']
#     title = og_title['content']
#     desc = og_description['content']

#     doc = {
#         'image':image,
#         'title':title,
#         'description':desc,
        
#     }

#     db.movies.insert_one(doc)

#     return jsonify({'msg':'POST request!'})


# @app.route("/movie", methods=["GET"])
# def movie_get():
#     movie_list = list(db.movies.find({},{'_id':False}))
#     return jsonify({'movies':movie_list})


# (Lihat semua data yang masuk di MongoDB)
# all_link = list(db.link.find({},{'_id':False}))

# print(all_link[0])         # Memperlihatkan hasil 0

# for link in all_link:      # loop through serta lihat seluruh hasilnya
#     print(link)



# (melihat hasil data totalnya ada berapa di dalam dokumen)
# count_clik = db.link.count_documents({'clik': '1'})
# count_instagram = db.link.count_documents({'instagram': '1'})
# count_whatsapp = db.link.count_documents({'whatsapp': '1'})

# # Print jumlah dokumen
# print(f"Jumlah dokumen dengan clik='1': {count_clik}")
# print(f"Jumlah dokumen dengan instagram='1': {count_instagram}")
# print(f"Jumlah dokumen dengan whatsapp='1': {count_whatsapp}")



# (menemukan data tertentu jumlahnya ada berapa)
# link = db.link.find_one({'clik': {'$exists': True}},{'_id':False} )
# print(link)

# @app.route("/movie", methods=["POST"])
# def movie_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg':'POST request!'})