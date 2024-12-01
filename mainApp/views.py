from django.shortcuts import render
from mainApp.langs import LANGUAGES
from googletrans import Translator

def show_app_page(request):
    return render(request, 'page.html', {"languages": LANGUAGES})


def translate_event(request):
    if request.method == "POST":
        try:    
            lang = request.POST.get("selectLang", None)
            txt = request.POST.get("inputText", None)
            translator = Translator()
            translated = translator.translate(txt, dest=lang)
            result = translated.text
            return render(request, 'page.html', {"result": result, "languages": LANGUAGES})
        except Exception as e:
            #print(e)
            result = "translate failed!"
            return render(request, 'page.html', {"result": result, "languages": LANGUAGES})
    return render(request, 'page.html')