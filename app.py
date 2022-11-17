import json
from flask import send_file,Flask, render_template, request, jsonify
from scapper import get_current_news
from pprint import pprint
import base64
import wave
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")

@app.route("/submitJSON", methods=["POST"])
def processJSON():
    jsonObj = request.get_json()
    #print(jsonStr)
    # pprint(jsonObj.keys())
    # print(jsonObj)
    temp1=jsonObj['search_val']
    response = ""
    response += '<img class="img-fluid w-100" src="static/img/news-500x280-3.jpg" style="object-fit: cover;">'
    # response +="Text you searched is <b>"+str(temp1)+"</b><br> <br>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br> Sit amet nisl purus in mollis nunc sed. In vitae turpis massa sed elementum tempus egestas sed sed. Interdum varius sit amet mattis vulputate enim nulla. Porttitor rhoncus dolor purus non enim. Nullam non nisi est sit.<br> Massa vitae tortor condimentum lacinia quis vel eros donec ac. At quis risus sed vulputate. Porttitor rhoncus dolor purus non enim praesent elementum. Ac odio tempor orci dapibus ultrices in iaculis. Nullam vehicula ipsum a arcu. Consectetur adipiscing elit ut aliquam purus.<br> "
    return response

@app.route("/loadNews", methods=["POST"])
def loadNews():
    jsonObj = request.get_json()
    print('reached api')
    current_news = get_current_news()
    news_dict = dict()

    for i, news in enumerate(current_news):
        news_dict[i] = news
    return json.dumps(news_dict)


# @app.route("/submitJSON1_", methods=["POST"])
# def processJSON1_():
#     jsonObj = request.get_json()
#     main_key = jsonObj['secret_key']

#     # file_id = jsonObj["audio_"].split('/')[-2]
#     # destination = 'my_file.wav'
#     # download_file_from_google_drive(file_id, destination)
#     e_path = os.getcwd()
#     audio_path = os.path.join(e_path, jsonObj['audio_'].split('\\')[-1])


#     with wave.open(audio_path, 'rb') as file:
#         arr=file.getparams()
#         f=file.readframes(100000)
    
#     e=base64.b64encode(f)
#     e=str(e, 'utf-8')
#     with open('encrypted_text.txt', 'w') as file:
#         file.write(e)
#     with open('parameters_audio.txt', 'w') as f:
#         for p in arr:
#             if p=='NONE':
#                 f.write(str(-1)+'\n')
#             elif p=='not compressed':
#                 f.write(str(-2)+'\n')
#             else:
#                 f.write(str(p)+'\n')
    
#     return "ok"
    
# @app.route("/get_file", methods=["GET"])
# def get_file():
#     response = 'encrypted_text.txt'
#     return send_file(response, 
#          mimetype="txt", 
#          as_attachment=True, 
#          attachment_filename="encrypted_text.txt")

# @app.route("/get_par_file", methods=["GET"])
# def get_par_file():
#     response = 'parameters_audio.txt'
#     return send_file(response, 
#          mimetype="txt", 
#          as_attachment=True, 
#          attachment_filename="parameters_audio.txt")

# @app.route("/submitJSON2_", methods=["POST"])
# def processJSON2_():
#     jsonObj = request.get_json()
#     main_key = jsonObj['secret_key'] 
#     e_path = os.getcwd()
#     encrypt_path = os.path.join(e_path, jsonObj['encrypted_text'].split('\\')[-1])
#     with open(encrypt_path, 'r') as file:
#         encrypted_line = file.read()
#     d = decrypt_text_with_gift64(encrypted_line, main_key)
#     d = bytes(d, 'utf-8')
#     d = base64.b64decode(d)
#     pars=[]
#     p_path = os.getcwd()
#     par_path = os.path.join(p_path, jsonObj['par_text'].split('\\')[-1])
#     with open(par_path, 'r') as f:
#         for line in f:
#             if int(line)==-1:
#                 pars.append('NONE')
#             elif int(line)==-2:
#                 pars.append('not compressed')
#             else:
#                 pars.append(int(line))
#     with wave.open('output_audio.wav', 'wb') as f:
#         f.setparams(pars)
#         f.writeframes(d)

#     return "ok"

# @app.route("/get_audio_file", methods=["GET"])
# def get_audio_file():
#     response = 'output_audio.wav'
#     return send_file(response, 
#          mimetype="txt", 
#          as_attachment=True, 
#          attachment_filename="Decrypted_audio.wav")


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=port, debug=True)
