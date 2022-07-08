import pandas as pd


def create_df():
    link1 = 'https://www.fu-berlin.de/studium/studienangebot/grundstaendige/informatik_mono/index.html'
    link2 = 'https://www.fu-berlin.de/studium/studienangebot/grundstaendige/bioinformatik_mono/index.html'
    link3 = 'https://www.hu-berlin.de/de/studium/beratung/angebot/sgb/infmono'
    link4 = 'https://www.tu.berlin/studieren/studienangebot/alle-studiengaenge/studiengang/informatik-b-sc'
    link5 = 'https://www.uni-hamburg.de/en/campuscenter/studienangebot/studiengang.html?1028562403'
    link6 = 'https://www.uva.nl/shared-content/programmas/en/bachelors/computational-social-science/computational-social-science.html'
    link7 = 'https://www.uva.nl/shared-content/programmas/en/bachelors/econometrics-and-operations-research/econometrics.html'
    link8 = 'https://www.uva.nl/programmas/bachelors/business-analytics/business-analytics.html'
    listof = []
    listof.append(['Berlin','fu-berlin', 'Informatik', 'German', 'Lokale Zulassungsbeschränkung', 'WS, Sos', '15.07.2022', f'<a target="_blank" href="{link1}">Hyperlink</a>'])
    listof.append(['Berlin','fu-berlin', 'Bioinformatik', 'German', 'Lokale Zulassungsbeschränkung', 'WS, Sos', '15.07.2022', f'<a target="_blank" href="{link2}">Hyperlink</a>'])
    listof.append(['Berlin','hu-berlin', 'Informatik', 'German', 'Nothing', 'WS, SuS', '15.07.2022', f'<a target="_blank" href="{link3}">Hyperlink</a>'])
    listof.append(['Berlin','tu-berlin', 'Informatik', 'German', 'Lokale Zulassungsbeschränkung', 'WS, Sos', '15.07.2022', f'<a target="_blank" href="{link4}">Hyperlink</a>'])
    listof.append(['Hamburg','uni-hamburg', 'Informatik', 'German', 'Numerus Clausus', 'WS', '15.07.2022', f'<a target="_blank" href="{link5}">Hyperlink</a>'])
    listof.append(['Amsterdam','uva', 'Computational Social Science', 'English', '10 points or higher in the Mathematics final examination', 'WS', '01.05.2022', f'<a target="_blank" href="{link6}">Hyperlink</a>'])
    listof.append(['Amsterdam','uva', 'Econometrics', 'English', '10 points or higher in the Mathematics final examination', 'WS', '01.05.2022', f'<a target="_blank" href="{link7}">Hyperlink</a>'])
    listof.append(['Amsterdam','uva', 'Business Analytics', 'English', '10 points or higher in the Mathematics final examination', 'WS', '01.05.2022', f'<a target="_blank" href="{link8}">Hyperlink</a>'])

    df = pd.DataFrame(listof,
        columns=('City','University', 'Study', 'Language', 'Acceptance', 'Starting', 'Deadline', 'Link'),
        index=[1,2,3,4,5,6,7,8])
    return df


