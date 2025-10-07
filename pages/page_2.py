import streamlit as st
import datetime

with st.form(key='profile_form'): # profile_formの部分の名前は自由（画面側からは見えない）
                                    # このwith文（内）を使用すれば、テキストボックスからカーソルが外れてもリロードされない
        # テキストボックス
        name = st.text_input('名前')            # 画面がリロードされた段階 or テキストボックスからカーソルが外れた段階で、戻り値nameにデータが入ってくる
        address = st.text_input('住所')

        # セレクトボックス
        age_category = st.radio( # ラジオボタンにしたい⇒st.selectboxをst.radioとすればOK
            '年齢層',
            ('子供（18才未満）','大人（18才以上）')
        )

        #複数選択
        hobby = st.multiselect( #選択されている値がリストで戻り値に格納される
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
        )

        # チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する')

        # スライダー
        height = st.slider('身長',min_value=110,max_value =210)

        # 日付
        start_date = st.date_input(
            '開始日',
            datetime.date(2025,10,7)
        )

        # カラーピッカー
        color =st.color_picker('テーマカラー','#00f900')


        # ボタン
        submit_btn = st.form_submit_button('送信')          # ボタンが押されている：True / ボタンが押されていない：False
        cancel_btn = st.form_submit_button('キャンセル')     # ボタンが押された瞬間リロード
        print(f'submit_btn:{submit_btn}')                   # python側で確認
        print(f'cancel_btn:{cancel_btn}')                   # with st.form(key='profile_form')を使用する場合は、st.buttonではなく、st.form_submit_buttonとする

        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味:{",".join(hobby)}') # 戻り値のリストをjoinを使用して、要素をカンマ区切りで結合した文字列に変換

