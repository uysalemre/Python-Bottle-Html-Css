from bottle import request, route, run, debug, default_app

username = "---"
password = "---"

iswheel = False
ismugen = False
isspoiler = False
issunshade = False
isvarex = False
choices = []

honda_counter = 0
bmw_counter = 0
nissan_counter = 0
audi_counter = 0
audi_counter = 0

owners_of_ap1 = [
    {'name': 'Hasan',
     'model': 1999,
     'birthplace': 'New York',
     'email': 'hasan16@itü.edu.tr'},

    {'name': 'Ali',
     'model': 2000,
     'birthplace': 'Kastamonu',
     'email': 'aali@itü.edu.tr'},

    {'name': 'Necmi',
     'model': 2002,
     'birthplace': 'Adana',
     'email': 'ppre@ytü.edu.tr'},

    {'name': 'Ekin',
     'model': 1999,
     'birthplace': 'Adana',
     'email': 'ekin@ytü.edu.tr'}

]

owners_of_ap2 = [
    {'name': 'Emre UYSAL',
     'model': 2009,
     'birthplace': 'New York',
     'email': 'uysalem16@itü.edu.tr'},

    {'name': 'Nisa YILDIRIM',
     'model': 2009,
     'birthplace': 'Kastamonu',
     'email': 'anısa@itü.edu.tr'},

    {'name': 'Ensar ESEN',
     'model': 2005,
     'birthplace': 'Adana',
     'email': 'ensaresen@ytü.edu.tr'},

    {'name': 'Eyüb ESEN',
     'model': 1999,
     'birthplace': 'Adana',
     'email': 'eyubesen@ytü.edu.tr'}

]

users = [
    {'username': 'fatihyilmaz',
     'password': ''},

    {'username': 'okanyildirim',
     'password': 'something'}
]
def html(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                  </head>
                  <style style="text/css">
                    body {  background-image: url("http://wallpapercave.com/wp/eFZOnap.jpg");
                            background-position: 90% 25%;
                             background-repeat:no-repeat;
                             color:white;
                        }
                    a {
                        color:white;}
                  </style>
                  <body>

                      """
    if (title == "Hello" or  title=="Sign Up") and username == "---":
        page += content
    elif title != "Hello" and username == "---":
        page += 'You have to log in <br /> <a href="/">Homepage</a>'
    elif title != "Hello" and username != "---":
        page += content
    else:
        page += content
    page += """
          </body>
          </html>"""
    return page

def index():
    welcome = "Hello stranger, welcome to my site!..."
    welcome += '''
        <form action="/login/" method="POST">
            Username: <input name="username" type="text" />
            </br>
            Password: <input name="password" type="password" />
            </br>
            <input value = "Login" type = "submit" />
        </form>
        <a href = /signup/>Sign Up</a>
    '''
    return  html("Hello", welcome)

def login():
    global username
    global password
    global users

    post_request = request.POST

    username = str(post_request['username'])
    password = str(post_request['password'])

    iscorrect = False

    for temp in users:
        if temp['username'] == username and temp['password'] == password:
            iscorrect = True
            break
        else:
            iscorrect = False

    if iscorrect :
        return  my_website()
    else:
        return login_failed()


def login_failed():
    content = "You are not an allowed user <br />"
    content += '<a href="/">Homepage</ a>'
    return html('Error', content)


def signup():
    title = 'Sign Up'

    content = '''<form method="POST" action="/signup_complete">\n
                 Userame: <input type="text" name="username" /><br />\n
                Password: <input type="password" name="password" /><br />\n
                 <input type="submit" value="Send" />\n
                </form>\n
            '''
    return html(title, content)

def signup_complete():
    global username
    global password
    global users
    post_request = request.POST
    username = str(post_request['username'])
    password = str(post_request['password'])

    users +=[{'username': username, 'password': password}]

    return index();

#####################################################333

def S2000_AP1():
    global model
    model = "ap1"
    content = '''<h1 align="center">AP1</h1><p >The S2000 was introduced in 1999 for the 2000 model year and was given the chassis designation of AP1. It features a front mid-engine, rear-wheel-drive layout with power delivered by a 1,997 cc (122 cu in) inline four-cylinder DOHC-VTEC engine. The engine (codenamed F20C) produces outputs of 177–184 kW (237–247 hp), and 208–218 N·m (153–161 lbf·ft) depending on the target market.[6] The engine is mated to a six-speed manual transmission and Torsen limited slip differential. The S2000 achieved what Honda claimed as the world's top level, high performance four-cylinder naturally aspirated engine.[7].Features include independent double wishbone suspension, electrically assisted steering and integrated roll hoops. The car features 16 in (41 cm) wheels with Bridgestone Potenza S-02 tires. The compact and lightweight engine, mounted entirely behind the front axle, allow the S2000 to achieve a 50:50 front/rear weight distribution and lower rotational inertia. An electrically powered vinyl top with internal cloth lining was standard, with an aluminum hardtop available as an optional extra (in 2001). Honda offered Berlina Black, New Formula Red, Gran Prix White, Sebring Silver and Silverstone Metallic in the US domestic market.
                            The 2001 model was largely unchanged; Honda added a digital clock to the radio display and made the rear wind blocker standard. Honda also added Spa Yellow to the US domestic market lineup. For the 2002 model year, suspension settings were revised and the plastic rear window was replaced by a glass unit incorporating an electric defroster. Other updates included slightly revised tail lamps with chrome rings, an upgraded radio with separate tweeters, a leather gearshift knob, leatherette console cover and a revised engine control unit. Honda added Suzuka Blue to the US domestic market lineup. The AP1 was manufactured up to 2003 at Honda's Takanezawa plant, alongside the Honda NSX and Honda Insight hybrid </p>
                             <fieldset>
                             <legend >IF YOU ARE AN AP1 OWNER JOIN AP1 CLUB:</legend>
                             '''+ header() +'''

                             </fieldset>
                             '''
    return html('AP1 S2000', content)


def S2000_AP2():
    global model
    model = "ap2"
    content = '''<h1 align="center" >AP2</h1><p>The 2004 model S2000 underwent several significant changes. Production moved to Suzuka. The new model introduced 17 in (43 cm) wheels and Bridgestone RE-050 tires along with a retuned suspension to reduce oversteer. The spring rates and shock absorber damping were altered and the suspension geometry modified to improve stability by reducing toe-in changes under cornering loads. The subframe also received a revision in design to achieve a high rigidity. In the gearbox the brass synchronizers were replaced with carbon fiber. In addition, cosmetic changes were made to the exterior with new front and rear bumpers, revised headlight assemblies, new LED tail-lights, and oval-tipped exhausts. Although all the cosmetic, suspension and most drivetrain upgrades were included on the Japanese, Australian and European S2000s, they retained the 2.0l F20C engines and remained designated as AP1s..For the North American market the updates also included the introduction of a larger version of the F20C (F22C1), this larger engine gave the chassis designation AP2. F22C1, the engine's stroke was lengthened, increasing its displacement to 2,157 cc (132 cu in). At the same time, the redline and fuel cutoff were reduced from 8,800 rpm and 9,000 rpm to 8,000 rpm and 8,200 rpm respectively, mandated by the longer travel of the pistons. Peak torque increased 6% to 220 N·m (160 lbf·ft) at 6,800 rpm while power output remained unchanged, 177 kW (237 hp) at a lower 7,800 rpm. In conjunction with its introduction of the F22C1, Honda also changed the transmission gear ratios by shortening the first five gears and lengthening the sixth.[10].In 2006, the F22C1 was also introduced to the Japanese market, with slightly higher outputs (178 kW (239 hp) and 221 N·m (163 lbf·ft)). The F20C continued in all other markets. The 2006 model introduced a drive by wire throttle, an electronic stability control system, new wheels, and one new exterior color, Laguna Blue Pearl. Interior changes included revised seats and additional stereo speakers integrated into the headrests.</p>
                             <fieldset >
                             <legend>IF YOU ARE AN AP2 OWNER JOIN AP2 CLUB:</legend>
                              '''+ header()+'''
                             </fieldset>
      '''


    return html('AP2 S2000', content)


def header():
    content = '''<nav>\n
                <ul>\n
                <li><a href="/list">List  Owners</a></li>\n
                <li><a href="/add">Join Us</a></li>\n
                <a href="/homepage/">Homepage</a> \n
                </ul>\n
                </nav>\n
            '''
    return content


def S2000_PARTS():
    global isvarex
    global issunshade
    global isspoiler
    global ismugen
    global iswheel
    global choices
    content = '''
    <form action="/upgrading">
        <input type="checkbox" name="filter" value ="wheel">Wheels</input>
        <input type="checkbox" name="filter" value ="mugen">Mugen Lip</input>
        <input type="checkbox" name="filter" value ="spoiler">Spoiler</input>
        <input type="checkbox" name="filter" value ="sunshade">Sunshade</input>
        <input type="checkbox" name="filter" value ="varex">Varex Exhaust</input>
        <input type="submit" value="Filter">
    </form>
    '''
    choices = request.query.getall('filter')
    print(choices)
    for temp in choices:
        if str(temp) == "wheel":
            iswheel = True
        if str(temp) == "mugen":
            ismugen = True
        if str(temp) == "spoiler":
            isspoiler = True
        if str(temp) == "sunshade":
            issunshade = True
        if str(temp) == "varex":
            isvarex = True



    content += """<h1 align="center" >WELCOME TO S2000 GARAGE AND SHOP</h1>"""
    if iswheel:
       content += '''
                <table align="center" width="258" border="0"><tr><th width="94" scope="col">WHEELS</th> <th width="12" scope="col">&nbsp;</th>
                <th width="62" scope="col">COST</th><th width="62" scope="col"> BUY</th></tr><tr><th scope="row">V1</th>
                <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQF9_7OP9iHTuRn8uqrHppsnpY0vZQ7x5XXf1H_-uzwRcMHgB_9fw" width="100" height="100" alt="V1"></td>
                <td> <div align="center">70TL</div></td><td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-jant-lastik-s2000-v1-jant-339687338/detay"><input type="submit" value="BUY"></form></td></tr>
                <tr><th scope="row">V2</th><td><img src="http://i.ebayimg.com/images/i/151904483876-0-1/s-l1000.jpg" width="100" height="100" alt="V2"></td>
                <td><div align="center">480TL</div></td><td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-jant-lastik-honda-s2000-v2-arka-tek-jant-8.5-sifir-aydinlas-performance-334930817/detay"><input type="submit" value="BUY"></form></td></tr><tr><th scope="row">V3</th>
                <td><img src="http://cimg7.ibsrv.net/gimg/www.s2ki.com-vbulletin/1600x1200/picture_php_pictureid_588775_f05c09058cfe71d67e9619aae38853d20fb66c87.jpg" width="100" height="100" alt="V3"></td>
                <td><div align="center">1500TL</div></td><td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-jant-lastik-honda-s2000-17-jant-v3-5x114-286303031/detay"><input name="submit" type="submit" value="BUY"></form></td> </tr>
                </table>
                '''
    content +=  '<table width="258"  align="center" border="0" >'
    if ismugen:
        content +=   '''

            <tr>
            <th scope="col">&nbsp;</th>
            <th scope="col">&nbsp;</th>
            </tr>
            <tr>
            <th scope="col">MUGEN LIP</th>
            <th scope="col"><img src="http://www.showoffimports.nl/images/T/230839.jpg" width="100" height="100" alt="MUGEN LIP"></th>
            <th scope="col">159TL</th>
            <th scope="col"><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-aksesuar-tuning-honda-s2000-on-lip-f2ktuning-den-378079634/detay"><input type="submit" value="BUY"></form></td></tr></th>
            </tr>
        '''
    if isspoiler:
        content += '''
            <tr>
            <th scope="row">SPOILER</th>
            <td><img src="http://www.fastautoworks.com/v/vspfiles/photos/TAMON-022-2.jpg" width="100" height="100" alt="SPOILER"></td>
            <td>95TL</td>
            <td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-aksesuar-tuning-s2000-spoiler-eb-garaj-374971535/detay"><input type="submit" value="BUY"></form></td></tr></td>
            </tr>
        '''
    if issunshade:
        content += '''
            <tr>
            <th scope="row">SUNSHADE</th>
            <td><img src="http://store.ceebaileys.com/v/vspfiles/photos/CS%20AUTO%20SHADES130-3.jpg" width="100" height="100" alt="sunshade"></form></td>
            <td>1000$</td>
            <td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-yedek-parca-honda-s2000-siyah-renk-tente-281347346/detay"><input type="submit" value="BUY"></form></td></tr></td>
            </tr>
        '''
    if isvarex:
        content += '''

            <tr>
            <th scope="row">VAREX EXHAUST</th>
            <td><img src="http://scontent.cdninstagram.com/t51.2885-15/s480x480/e35/c68.0.720.720/11821955_446762345516570_1559664610_n.jpg?ig_cache_key=MTA3NjAwNTI3NDU0NDg3MTIyNw%3D%3D.2.c" width="100" height="100" alt="VAREX"></td>
            <td>350TL</td>
            <td><form method="link" action="https://www.sahibinden.com/ilan/yedek-parca-aksesuar-donanim-tuning-otomotiv-ekipmanlari-aksesuar-tuning-varex-style-egsoz-kurom-paslanmaz-faturali-kapida-odeme-egzoz-341205899/detay">
            <input type="submit" value="BUY"></form> </td></tr></td>
            </tr>
        '''
    content += '</table>'


    iswheel = False
    ismugen = False
    isspoiler = False
    issunshade = False
    isvarex = False
    return html('GARAGE AND SHOP', content)


def my_website():
    content =   """
                   <h1  style="text-align:center;">HONDA S2000</h1>
                    <p style="clear:both;">The Honda S2000 was a roadster that was manufactured by Japanese automaker Honda from 1999 to 2009.<br> First shown as a concept car at the Tokyo Motor Show in 1995, the production version was launched in April 1999 to celebrate the company's 50th anniversary.<br> The S2000 is named for its engine displacement of two liters, carrying on in the tradition of the S500, S600, and S800 roadsters of the 1960s.
                    Several revisions were made throughout the car's lifetime, including changes to the engine, gearbox, suspension, interior and exterior.<br> Officially two variants exist: the initial launch model was given the chassis code AP1, though cosmetically similar, the facelifted version (known as the AP2 in the US) incorporated significant changes to the drivetrain and suspension. Production of the S2000 ceased in June 2009. In Japan, it was exclusively sold through the Honda Verno sales channel.    </p>
                    <h3>Which one attracted you more?</h3>
                    <form method ="POST" action="/selection_of_model/">
                      <input type="radio" name="model" value="Ap1"> Ap1<br />
                      <input type="radio" name="model" value="Ap2"> Ap2<br />
                      <input value = "Select" type = "submit" />
                    </form>
                    <h1  align="right" style=" float:right:"><a href="/upgrading">UPGRADE YOUR S2K</a></h1>
                    <h1  align="right" style=" float:right:"><a href="/survey">Survey</a></h1>
                """

    return html('HONDA S2000 HOME', content)

############################################################################################################################
############################################################################################################################
############################################################################################################################

def survey():
    content = '''
                <h1>What is your favorite Roadster type car?</h1>
                 <form method ="POST" action="/results">
                <table width="258"  align="center" border="0">
                    <tr>
                    <td>HONDA</td>
                    <td><img src="http://www.showoffimports.nl/images/T/230839.jpg" width="100" height="100" alt="Honda"></td>
                    <td><input type="radio" name="model" value="honda"><br /></td>
                    </tr>
                    <tr>
                    <td>BMW</td>
                    <td><img src="http://www.arabamoto.com/var/albums/BMW/BMW-AC-Schnitzer-ACS4-M-Roadster/BMW_AC_Schnitzer_ACS4_M_Roadster-araba_resim_galeri.jpg" width="100" height="100" alt="BMW"></td>
                    <td><input type="radio" name="model" value="bmw"><br /></td>
                    </tr>
                    <tr>
                    <td>NISSAN</td>
                    <td><img src="http://www.eurweb.com/wp-content/uploads/2012/08/370_roadster2012-wide.jpg" width="100" height="100" alt="Nissan"></td>
                    <td><input type="radio" name="model" value="nissan"><br /></td>
                    </tr>
                    <tr>
                    <td>AUDI</td>
                    <td><img src="http://cdn.sifirarabakampanyalari.org/wp-content/uploads/2016/04/Yeni-model-arabalar-2017-Audi-TT-RS-Roadster-21.jpg" width="100" height="100" alt="Audi"></td>
                    <td><input type="radio" name="model" value="audi"><br /></td>
                    </tr>
                    <tr>
                    <td></td>
                    <td><input type="submit" value="Submit" /></td>
                    <td></td>
                    </tr>
                    </table>

                </form>
    '''
    return html("survey", content)


def results():
    global honda_counter
    global bmw_counter
    global nissan_counter
    global audi_counter

    model = str(request.forms.get('model'))
    print(model)
    if model == "honda":
        honda_counter +=1
    elif model== "bmw":
        bmw_counter += 1
    elif model == "nissan":
        nissan_counter += 1
    elif model == "audi":
        audi_counter += 1

    content = '<h3>HONDA:'  + str(honda_counter) +  '</h3>'
    content += '<h3>BMW:'  + str(bmw_counter) +  '</h3>'
    content += '<h3>NISSAN:'  + str(nissan_counter) +  '</h3>'
    content += '<h3>AUDI:'  + str(audi_counter) +  '</h3>'
    content += '<a href=/survey>Back</ a>'
    return html("Results", content)

def selection_of_model():
    model = str(request.forms.get('model'))
    if model == "Ap1":
        return S2000_AP1()
    elif model == "Ap2":
        return S2000_AP2()


def list_page():

    content = '''  <table>\n
                     <tr>\n
                     <th>Name</th>\n
                     <th>Birth Year</th>\n
                     <th>Birth Place</th>\n
                     <th>E-mail Address</th>\n
                     <th></th>\n
                     </tr>\n
              '''

    if model == "ap1":

        title = 'AP1 CLUB'

        for person in owners_of_ap1:
            content +=  '  <tr>\n'
            content +=  '    <td>' + str(person['name']) + '</td>\n'
            content +=  '    <td>' + str(person['model']) + '</td>\n'
            content +=  '    <td>' + str(person['birthplace']) + '</td>\n'
            content +=  '    <td>' + str(person['email']) + '</td>\n'
            content +=  '    <td>\n'
            content +=  '      <form method="GET" action="/update/' + str(person['name']) + '">\n'
            content +=  '        <input type="submit" value="Update" />\n'
            content +=  '      </form>\n'
            content +=  '    </td>\n'
            content +=  '  </tr>\n'

        content +=  '</table>\n'
        content += '<a href="/ap1/">Back</a>'
    elif model == "ap2":
        title = 'AP2 CLUB'

        for person in owners_of_ap2:
            content +=  '  <tr>\n'
            content +=  '    <td>' + str(person['name']) + '</td>\n'
            content +=  '    <td>' + str(person['model']) + '</td>\n'
            content +=  '    <td>' + str(person['birthplace']) + '</td>\n'
            content +=  '    <td>' + str(person['email']) + '</td>\n'
            content +=  '    <td>\n'
            content +=  '      <form method="GET" action="/update/' + str(person['name']) + '">\n'
            content +=  '        <input type="submit" value="Update" />\n'
            content +=  '      </form>\n'
            content +=  '    </td>\n'
            content +=  '  </tr>\n'

        content += '</table>\n'
        content += '<a href="/ap2/">Back</a>'

    return html(title, content)


def search_by_name(name, people):
    for person in people:
        if person['name'] == name:
            return person

def update_page(name):
    title = 'Update'
    if model == "ap1":

        global owners_of_ap1
        person = search_by_name(name, owners_of_ap1)

        content = '<form method="POST" action="/update_submit">\n'
        content +=  '  Name: <input  type="text" name="name" value="' + str(person['name']) + '" readonly /><br />\n'
        content +=  '  Birth Year: <input type="number" name="model" value=' + str(person['model']) + ' /><br />\n'
        content +=  '  Birth Place: <input type="text" name="birthplace" value="' + str(person['birthplace']) + '" /><br />\n'
        content +=  '  E-mail Address: <input type="email" name="email" value="' + str(person['email']) + '" /><br />\n'
        content +=  '  <input type="submit" value="Update" />\n'
        content +=  '</form>\n'

    elif model == "ap2":

        global owners_of_ap2
        person = search_by_name(name, owners_of_ap2)

        content =  '<form method="POST" action="/update_submit">\n'
        content +=  '  Name: <input  type="text" name="name" value="' + str(person['name']) + '" readonly /><br />\n'
        content +=  '  Birth Year: <input type="number" name="model" value=' + str(person['model']) + ' /><br />\n'
        content +=  '  Birth Place: <input type="text" name="birthplace" value="' + str(person['birthplace']) + '" /><br />\n'
        content +=  '  E-mail Address: <input type="email" name="email" value="' + str(person['email']) + '" /><br />\n'
        content +=  '  <input type="submit" value="Update" />\n'
        content +=  '</form>\n'

    return html(title, content)


def update_submit_page():
    title = 'JOIN AP1 CLUB'
    post_request = request.POST

    name = str(post_request['name'])
    byear = int(post_request['model'])
    birthplace = str(post_request['birthplace'])
    email = str(post_request['email'])


    if model == "ap1":

        person = search_by_name(name, owners_of_ap1)
        person['name'] = name
        person['model'] = byear
        person['birthplace'] = birthplace
        person['email'] = email

        content =  '<p>Updated the following person:</p>\n'
        content +=  '<table >\n'
        content +=  '  <tr>\n'
        content +=  '    <th>Name</th>\n'
        content +=  '    <th>Birth Year</th>\n'
        content +=  '    <th>Birth Place</th>\n'
        content +=  '    <th>E-mail Address</th>\n'
        content +=  '  </tr>\n'
        content +=  '  <tr>\n'
        content +=  '    <td>' + str(name) + '</td>\n'
        content +=  '    <td>' + str(byear) + '</td>\n'
        content +=  '    <td>' + str(birthplace) + '</td>\n'
        content +=  '    <td>' + str(email) + '</td>\n'
        content +=  '  </tr>\n'
        content +=  '</table>\n'
    elif model == "ap2":

        person = search_by_name(name, owners_of_ap2)
        person['name'] = name
        person['model'] = byear
        person['birthplace'] = birthplace
        person['email'] = email

        content =   '<p>Updated the following person:</p>\n'
        content +=  '<table >\n'
        content +=  '  <tr>\n'
        content +=  '    <th>Name</th>\n'
        content +=  '    <th>Birth Year</th>\n'
        content +=  '    <th>Birth Place</th>\n'
        content +=  '    <th>E-mail Address</th>\n'
        content +=  '  </tr>\n'
        content +=  '  <tr>\n'
        content +=  '    <td>' + str(name) + '</td>\n'
        content +=  '    <td>' + str(byear) + '</td>\n'
        content +=  '    <td>' + str(birthplace) + '</td>\n'
        content +=  '    <td>' + str(email) + '</td>\n'
        content +=  '  </tr>\n'
        content +=  '</table>\n'
    content += '<a href="/list">Back</a>'
    return html(title, content)


def add_page():
    title = 'JOIN AP1 CLUB'

    content =   '<form method="POST" action="/add_submit">\n'
    content +=  '  Name: <input type="text" name="name" /><br />\n'
    content +=  '  Birth Year: <input type="number" name="model" /><br />\n'
    content +=  '  Birth Place: <input type="text" name="birthplace" /><br />\n'
    content +=  '  E-mail Address: <input type="email" name="email" /><br />\n'
    content +=  '  <input type="submit" value="Add" />\n'
    content +=  '</form>\n'

    return html(title, content)


def add_submit_page():
    title = 'JOIN US'

    post_request = request.POST
    name = str(post_request['name'])
    byear = int(post_request['model'])
    birthplace = str(post_request['birthplace'])
    email = str(post_request['email'])
    content = ""
    if model == "ap1":
        global  owners_of_ap1
        owners_of_ap1 += [{'name': name, 'model': byear, 'birthplace': birthplace, 'email': email}]

        content =   '<p>Added the following person:</p>\n'
        content +=  '<table>\n'
        content +=  '  <tr>\n'
        content +=  '    <th>Name</th>\n'
        content +=  '    <th>Birth Year</th>\n'
        content +=  '    <th>Birth Place</th>\n'
        content +=  '    <th>E-mail Address</th>\n'
        content +=  '  </tr>\n'
        content +=  '  <tr>\n'
        content +=  '    <td>' + str(name) + '</td>\n'
        content +=  '    <td>' + str(byear) + '</td>\n'
        content +=  '    <td>' + str(birthplace) + '</td>\n'
        content +=  '    <td>' + str(email) + '</td>\n'
        content +=  '  </tr>\n'
        content +=  '</table>\n'
    elif model == "ap2":
        global owners_of_ap2
        owners_of_ap2 += [{'name': name, 'model': byear, 'birthplace': birthplace, 'email': email}]

        content =   '<p>Added the following person:</p>\n'
        content +=  '<table>\n'
        content +=  '  <tr>\n'
        content +=  '    <th>Name</th>\n'
        content +=  '    <th>Birth Year</th>\n'
        content +=  '    <th>Birth Place</th>\n'
        content +=  '    <th>E-mail Address</th>\n'
        content +=  '  </tr>\n'
        content +=  '  <tr>\n'
        content +=  '    <td>' + str(name) + '</td>\n'
        content +=  '    <td>' + str(byear) + '</td>\n'
        content +=  '    <td>' + str(birthplace) + '</td>\n'
        content +=  '    <td>' + str(email) + '</td>\n'
        content +=  '  </tr>\n'
        content +=  '</table>\n'

    content += '<a href="/list">Back</a>'
    return html(title, content)


######################################################################################################################################################
######################################################################################################################################################


route('/','GET',index)
route('/login/', 'POST', login)
route('/signup/', 'GET', signup)
route('/signup_complete', 'POST', signup_complete)
route('/selection_of_model/', 'POST', selection_of_model)
route('/homepage/', 'GET', my_website)


route('/update/<name>', 'GET', update_page)
route('/list', 'GET', list_page)
route('/update_submit', 'POST', update_submit_page)
route('/add', 'GET', add_page)
route('/add_submit', 'POST', add_submit_page)


route('/upgrading','GET',S2000_PARTS)
route('/survey', 'GET', survey)
route('/results', 'POST', results)

route('/ap2/','GET',S2000_AP2)
route('/ap1/', 'GET', S2000_AP1)

route('/assignment3/', 'GET', index)

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

