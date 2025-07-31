from flask import Flask, render_template, request
import difflib

# Impor fungsi refactor (akan dibuat nanti)
# from .refactor import refactor_code

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Menangani permintaan GET dan POST ke rute root.
    Pada permintaan POST, ia menerima kode, merefaktornya, dan menampilkan perbandingannya.
    """
    if request.method == 'POST':
        original_code = request.form.get('code', '')

        # Placeholder untuk logika refaktorisasi AI
        # Untuk MVP ini, kita akan menggunakan fungsi simulasi.
        # refactored_code = refactor_code(original_code)

        # Contoh refaktorisasi sederhana untuk demonstrasi
        refactored_code = original_code.replace("range(len(", "enumerate(")

        # Hasilkan perbandingan diff
        diff = difflib.HtmlDiff(wrapcolumn=80).make_table(
            original_code.splitlines(keepends=True),
            refactored_code.splitlines(keepends=True),
            fromdesc='Kode Asli',
            todesc='Kode yang Direfaktor'
        )

        return render_template('index.html', diff=diff, original_code=original_code)

    return render_template('index.html', diff=None, original_code='')

if __name__ == '__main__':
    # Menjalankan aplikasi dalam mode debug untuk pengembangan
    app.run(debug=True)
