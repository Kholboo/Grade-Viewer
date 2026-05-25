from flask import Flask, request, send_file, jsonify
import pandas as pd
import os
#1-b, 2-b, 3-b, 4-b, 5-b, 6-b, 7-b, 8-b, 9-b,10-b,11-a,12-a,13-a,14-a,15-b
app = Flask(__name__)

# Энэ функцийг та өөрийн тестийн зөв хариултуудтай тааруулж хөгжүүлнэ
def process_test_image(image_path):
    # Жишээ: Зургийг OpenCV-ээр уншаад, текст эсвэл дугуйлсан хариуг танина
    # Одоогоор туршилтын хиймэл өгөгдөл буцааж байна:
    student_name = "Бат-Эрдэнэ" 
    score = 85  # 100-аас
    total_questions = 20
    correct_answers = 17
    
    return {
        "Сурагчийн нэр": student_name,
        "Нийт асуулт": total_questions,
        "Зөв хариулсан": correct_answers,
        "Оноо (%)": score
    }

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist("files")
    data_list = []

    for file in uploaded_files:
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)
        
        # Зургийг боловсруулах
        result = process_test_image(filepath)
        data_list.append(result)
        
        # Ашигласан зургийг устгах (сонголттой)
        os.remove(filepath)

    # Жагсаалтыг Excel (Pandas) руу хөрвүүлэх
    df = pd.DataFrame(data_list)
    excel_path = "results/Тестийн_Дүн.xlsx"
    df.to_excel(excel_path, index=False)

    return jsonify({"status": "success", "download_url": "/download-excel"})

@app.route('/download-excel', methods=['GET'])
def download_excel():
    return send_file("results/Тестийн_Дүн.xlsx", as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('uploads'): os.makedirs('uploads')
    if not os.path.exists('results'): os.makedirs('results')
    app.run(debug=True, port=5000)