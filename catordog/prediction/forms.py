from django import forms #Djangoからformsモジュールをインポート
#formsモジュールはユーザーからのデータ入力を管理できる便利なクラスやメソッドを提供している

#formsモジュールのFormクラスを継承し、画像をアップロードするためのImageUploadFormクラスを定義する
#forms.FormはDjangoのフォームを作成するための基底クラス（親クラス）である
#フォームの基本的な機能が実装されている

class ImageUploadForm(forms.Form):


#画像アップロードのフィールドを定義し、image変数に代入する
#アップロードするべきファイルが画像形式である場合、forms.ImageField()を利用する
#forms.ImageFieldで、フォームに画像をアップロードするための入力欄を作成できる
    image = forms.ImageField()
