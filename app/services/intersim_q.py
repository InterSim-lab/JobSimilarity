import pandas as pd
import random
import json
import re

answer = [
      {
        "id": "q1",
        "answer": "Saya sangat senang dan bersemangat untuk wawancara ini. Saya berharap dapat mempelajari lebih banyak tentang posisi ini dan bagaimana saya dapat berkontribusi pada perusahaan.",
        "type": "opening"
      },
      {
        "id": "q2",
        "answer": "Saya memiliki latar belakang pendidikan di bidang Ilmu Komputer dan memiliki pengalaman kerja selama 5 tahun sebagai pengembang perangkat lunak. Saya memiliki spesialisasi di bidang AI generative dan Python.",
        "type": "background"
      },
      {
        "id": "q3",
        "answer": "Saya mempertahankan pengetahuan dan keterampilan saya di bidang AI generative dan Python dengan membaca artikel dan paper ilmiah terbaru, serta mengikuti kursus dan pelatihan online.",
        "type": "background"
      },
      {
        "id": "q4",
        "answer": "Saya mengintegrasikan model AI generative ke dalam aplikasi menggunakan Python dan framework seperti TensorFlow dan PyTorch. Sebagai contoh, saya pernah mengembangkan aplikasi chatbot yang menggunakan model AI generative untuk menghasilkan respon yang lebih akurat.",
        "type": "technical"
      },
      {
        "id": "q5",
        "answer": "Saya mengoptimalkan kode untuk efisiensi dan skalabilitas dengan menggunakan tools seperti PyCharm dan Jupyter Notebook. Saya juga menggunakan teknik seperti caching dan parallel processing untuk meningkatkan kinerja aplikasi.",
        "type": "technical"
      },
      {
        "id": "q6",
        "answer": "Saya menangani kesalahan dan melakukan debugging dalam kode Python dengan menggunakan tools seperti print() dan pdb. Sebagai contoh, saya pernah menemukan kesalahan dalam kode saya dengan menggunakan teknik debugging tersebut.",
        "type": "technical"
      },
      {
        "id": "q7",
        "answer": "Saya bekerja dengan tim untuk mengembangkan aplikasi yang menggunakan teknologi AI generative dengan melakukan komunikasi yang efektif dan melakukan testing yang teliti. Sebagai contoh, saya pernah berkolaborasi dengan tim untuk mengembangkan aplikasi pengenalan gambar yang menggunakan teknologi AI generative.",
        "type": "behavioral"
      },
      {
        "id": "q8",
        "answer": "Saya menangani konflik atau perbedaan pendapat dalam tim pengembangan dengan melakukan komunikasi yang terbuka dan melakukan diskusi yang konstruktif. Sebagai contoh, saya pernah menyelesaikan konflik dalam tim dengan melakukan mediasi dan mencari solusi yang dapat diterima semua pihak.",
        "type": "behavioral"
      },
      {
        "id": "q9",
        "answer": "Tujuan karier saya dalam beberapa tahun ke depan adalah untuk menjadi ahli di bidang AI generative dan Python. Saya melihat peran ini dapat membantu saya mencapai tujuan tersebut dengan memberikan saya kesempatan untuk berkontribusi pada pengembangan aplikasi yang inovatif.",
        "type": "career discussion"
      },
      {
        "id": "q10",
        "answer": "Saya siap untuk bergabung dengan kantor dalam waktu 2 minggu. Saya tidak memiliki masa kontrak yang masih berlaku.",
        "type": "logistics"
      },
      {
        "id": "closing",
        "statement": "Terima kasih atas waktu Anda hari ini! Saya sangat senang dapat melakukan wawancara ini dan berharap dapat bergabung dengan tim Anda.",
        "type": "closing"
      }
    ]
question = [
    {"id": "q1", "question": "Bagaimana perjalanan Anda hari ini? Ada hal yang menyenangkan atau menarik?", "type": "opening"},
    {"id": "q2", "question": "Sebelum kita memulai, dapatkah Anda memberi tahu kami tentang pengalaman kerja Anda sebelumnya?", "type": "opening"},
    {"id": "q3", "question": "Dapatkah Anda menceritakan tentang latar belakang pendidikan Anda? Bagaimana Anda menghubungkannya dengan posisi Desk Collection ini?", "type": "background"},
    {"id": "q4", "question": "Berapa lama Anda telah bekerja di industri fintech? Bagaimana Anda mengembangkan kemampuan Anda dalam berkomunikasi dengan pelanggan?", "type": "background"},
    {"id": "q5", "question": "Dalam sebuah kasus, Pelanggan memiliki tunggakan pembayaran yang besar. Bagaimana Anda akan menangani situasi ini dan tetap menjaga hubungan baik dengan pelanggan?", "type": "technical_assessment"},
    {"id": "q6", "question": "Bagaimana Anda akan memprioritaskan tugas dan manajemen waktu ketika Anda memiliki beberapa akun yang perlu dihubungi?", "type": "technical_assessment"},
    {"id": "q7", "question": "Dapatkah Anda memberi contoh tentang strategi koleksi yang efektif yang pernah Anda gunakan? Bagaimana Anda mengukur keberhasilannya?", "type": "technical_assessment"},
    {"id": "q8", "question": "Dalam sebuah tim, Anda memiliki rekan kerja yang kurang memiliki kemampuan dalam berkomunikasi dengan pelanggan. Bagaimana Anda akan membantu rekan kerja Anda itu?", "type": "behavioral_soft_skills"},
    {"id": "q9", "question": "Pernahkah Anda menghadapi kegagalan dalam koleksi? Bagaimana Anda mengatasi dan belajar dari kegagalan itu?", "type": "behavioral_soft_skills"},
    {"id": "q10", "question": "Apa yang membuat Anda tertarik dengan peran Desk Collection di Kredivo Group? Bagaimana Anda melihat posisi ini dapat membantu Anda mencapai tujuan karier Anda?", "type": "career_discussion"},
    {"id": "q11", "question": "Kapan Anda dapat bergabung dengan tim kita?", "type": "logistics_next_steps"},
    {"id": "closing", "statement": "Terima kasih banyak atas waktu Anda hari ini. Kami akan segera menghubungi Anda untuk memberi tahu status aplikasi Anda. Selamat siang!", "type": "closing"}
]

class InterSim:
    def __init__(self, data_path: str = "data/QS-syntetic.csv"):
        self.df = pd.read_csv(data_path)
        self.SGenerator = self.df["output_text"]

    def generator(self, type: str):
        if type.lower() == "q":
            return {"questions": answer, "answers": answer}
            
        elif type.lower() == "s":
            num_random = random.randint(0, len(self.df) - 1)
            return self.SGenerator[num_random]
        else:
            return json.dumps({"error": "Invalid type"})