import tkinter as tk
from tkinter import messagebox
import json 

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("لوحة تحكم المخزن الذكي v1.0")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0") # لون خلفية مريح للعين

        # --- العنوان الرئيسي ---
        self.title_label = tk.Label(root, text="نظام إدارة المنتجات", font=("Cairo", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        # --- منطقة الإدخال (النماذج - Forms) ---
        self.frame_inputs = tk.Frame(root, bg="#f0f0f0")
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="اسم المنتج:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_inputs)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self.frame_inputs, text="السعر:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.entry_price = tk.Entry(self.frame_inputs)
        self.entry_price.grid(row=1, column=1)

        # --- الأزرار ---
        self.btn_add = tk.Button(root, text="إضافة منتج +", command=self.add_product, bg="#28a745", fg="white", width=15)
        self.btn_add.pack(pady=10)

        # --- قائمة العرض (المكان الذي ستظهر فيه المنتجات) ---
        self.product_list = tk.Listbox(root, width=70, height=10)
        self.product_list.pack(pady=20, padx=20)
        self.load_data() # لقراءة البيانات فور فتح البرنامج

    def add_product(self):

        name = self.entry_name.get()
        price = self.entry_price.get()
        
        if name and price:
            # أولاً: الحفظ في ملف JSON (المنطق الذي تدربنا عليه أمس)
            new_item = {"name": name, "price": price}
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except:
                data = []
            
            data.append(new_item)
            
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            # ثانياً: العرض في الواجهة الرسومية (التي نراها الآن)
            display_text = f"المنتج: {name} | السعر: {price} $"
            self.product_list.insert(tk.END, display_text)
            
            # ثالثاً: تنظيف الحقول
            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            messagebox.showinfo("نجاح", "تم حفظ المنتج في الملف والواجهة!")
        else:
            messagebox.showwarning("تنبيه", "يرجى ملء جميع الحقول!")

    def load_data(self):
        try:
            with open("data.json","r") as f:
                data = json.load(f)
                for item in data:
                    display_text = f"product : {item['name']} | price : {item['price']}$"

                    self.product_list.insert(tk.END, display_text)
        
        except FileNotFoundError:
            pass

# تشغيل التطبيق
if __name__ == "__main__":
    window = tk.Tk()
    app = InventoryApp(window)
    window.mainloop()


