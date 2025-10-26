import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from PyPDF2 import PdfReader
from transformers import pipeline

# ---- Özetleme modeli ----
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ---- GUI oluştur ----
root = tk.Tk()
root.title("PDF Belge Özetleyici")
root.geometry("1000x700")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_load = tk.Button(frame, text="📂 PDF Yükle", bg="#4CAF50", fg="white", width=20)
btn_load.grid(row=0, column=0, padx=10)

btn_summarize = tk.Button(frame, text="🧠 Özetle", bg="#2196F3", fg="white", width=20)
btn_summarize.grid(row=0, column=1, padx=10)

input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=120, height=20)
input_box.pack(padx=10, pady=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=120, height=10, bg="#f9f9f9")
output_box.pack(padx=10, pady=10)

pdf_text = ""


# ---- PDF yükleme ----
def load_pdf():
    global pdf_text
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return
    try:
        reader = PdfReader(file_path)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"
        input_box.delete(1.0, tk.END)
        input_box.insert(tk.END, pdf_text.strip())
        messagebox.showinfo("PDF Yüklendi", f"{len(reader.pages)} sayfa başarıyla okundu.")
    except Exception as e:
        messagebox.showerror("Hata", f"PDF okunamadı:\n{e}")


# ---- Özetleme işlemi ----
def summarize_pdf():
    text = input_box.get(1.0, tk.END).strip()
    if not text:
        messagebox.showwarning("Uyarı", "Lütfen bir PDF yükle veya metin gir.")
        return

    max_len = 1024  # Modelin kapasitesi (token sınırı)
    text = text[:max_len * 4]  # Çok uzun metinleri kırpıyoruz (yaklaşık 4 token/kelime)
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]["summary_text"]

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, summary)


btn_load.config(command=load_pdf)
btn_summarize.config(command=summarize_pdf)

root.mainloop()
