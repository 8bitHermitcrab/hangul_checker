import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from hanspell import spell_checker


def check_spelling():
    text = text_input.get("1.0", tk.END)
    label4.config(text=len(text))

    paragraphs = text.split("\n\n")
    checked = ""
    errors = 0
    time = 0
    
    # 500자 제한 해결
    for paragraph in paragraphs:
        if len(paragraph) > 500:
            list_txt = [text[i:i+500] for i in range(0, len(paragraph), 500)]
            for i in list_txt:
                result = spell_checker.check(i)
                res_dict = result.as_dict()   # dict로 출력
                checked += res_dict['checked']
                errors += int(res_dict['errors'])
                time += float(res_dict['time'])
            # 문단 구분 추가
            checked += "\n\n"

        # 500자 안 될 때
        else:
            result = spell_checker.check(paragraph)
            res_dict = result.as_dict()   # dict로 출력
            checked += res_dict['checked']
            errors += res_dict['errors']
            time += res_dict['time']
            # 문단 구분 추가
            checked += "\n\n"

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.INSERT, checked)
    label6.config(text=errors)
    label8.config(text=time)
    messagebox.showinfo("알림", "맞춤법 검사 완료")

def copy_to_clipboard():
    text = text_output.get("1.0", tk.END)
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("알림", "결과가 클립보드 복사 완료")


# 1. 루트화면 (root window) 생성
window = tk.Tk()
window.title("한글 맞춤법 검사기")
# 500x500 크기의 창 생성, 좌표 x500, y150
window.geometry("500x500+500+150")
# 창 크기 조절
window.resizable(True, True)

# 2. 텍스트 표시
text_input = scrolledtext.ScrolledText(window, height=10)
text_input.pack()

check_button = tk.Button(window, text='맞춤법 검사', command=check_spelling)
check_button.pack()

# 결과 출력 텍스트 박스
text_output = scrolledtext.ScrolledText(window, height=10)
text_output.pack()

# 클립보드에 복사 버튼
copy_button = tk.Button(window, text="결과를 클립보드에 복사", command=copy_to_clipboard)
copy_button.pack()

label3 = tk.Label(window, text='총 글자수 : ')
label4 = tk.Label(window, text='0')
label3.pack()
label4.pack()

label5 = tk.Label(window, text='맞춤법 오류 개수 : ')
label6 = tk.Label(window, text='0')
label5.pack()
label6.pack()

label7 = tk.Label(window, text='걸린 시간 : ')
label8 = tk.Label(window, text='0')
label7.pack()
label8.pack()

# 4. 메인루프 실행
window.mainloop()