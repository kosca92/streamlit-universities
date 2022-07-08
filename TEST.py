data = {'name': ['Tom', 'nick', 'krish', 'jack', 'Tom'],
        'nickname': ['jack', 'krish', 'karim', 'joe', 'joe'],
        'age': [20, 18, 19, 18, 22]}

df = pd.DataFrame(data)
st.write(df)
df_result_search = pd.DataFrame()

searchcheckbox_name_nickname = st.checkbox("Name or Nickname ", value=False, key=1)
searchcheckbox_age = st.checkbox("age", value=False, key=2)

if searchcheckbox_name_nickname:
    name_search = st.text_input("name")
    nickname_search = st.text_input("nickname")
else:
    name_search = ''
    nickname_search = ''

if searchcheckbox_age:
    age_search = st.number_input("age", min_value=0)
else:
    age_search = 0

if st.button("search"):
    # 1. only name/nickname is checked
    if searchcheckbox_name_nickname and not searchcheckbox_age:
        # if name is specified but not the nickname
        if name_search != '' and nickname_search == '':
            df_result_search = df[df['name'].str.contains(name_search, case=False, na=False)]
        # if nickname is specified but not the name
        elif name_search == '' and nickname_search != '':
            df_result_search = df[df['nickname'].str.contains(nickname_search, case=False, na=False)]
        # if both name and nickname are specified
        elif name_search != '' and nickname_search != '':
            df_result_search = df[(df['name'].str.contains(name_search, case=False, na=False)) & (
                df['nickname'].str.contains(nickname_search, case=False, na=False))]
        # if user does not enter anything
        else:
            st.warning('Please enter at least a name or a nickname')

    # 2. only age is checked
    elif not searchcheckbox_name_nickname and searchcheckbox_age:
        if age_search != 0:
            df_result_search = df[df['age'] == age_search]

    # 3. if both name/nickname and age are checked
    else:
        pass  # continue here.

    st.write("{} Records ".format(str(df_result_search.shape[0])))
    st.dataframe(df_result_search)