#!/usr/bin/python3



# Import speeech recognition  module
import speech_recognition as sr

from gtts import gTTS
import os



language = 'en'




def recognize_speech():
    # create instance of Recognizer class
    r = sr.Recognizer()

    # create instance of physical microphone
    mic = sr.Microphone()


    with mic as source:
        # adjust noise
        r.adjust_for_ambient_noise(source)
        print('Say somtheing')
        # listen audio from microphone
        audio = r.listen(source)


    # Recognize audio using google api
    print("Now recognize ")
    return (r.recognize_google(audio)).lower()
    # text=r.recognize_sphinx(audio)
    # subprocess.getoutput(text)




def text_to_speech(text):
    gtts_obj = gTTS(text = text , lang = language , slow=False)
    gtts_obj.save('/tmp/test.mp3')
    os.system('mpg321 /tmp/test.mp3 -quiet')



usr_input = recognize_speech()

if 'directory'in usr_input or 'folder' in usr_input :
    if 'create' in usr_input or 'make' in usr_input:
        text_to_speech('What\'s the directory name ' )
        dir_name = recognize_speech()
        text_to_speech('Specify path under home')
        path = recognize_speech()
        print('******* {} '.format(path))


        exact_path = os.listdir('/home/pybot/')

        for i in exact_path:
            if i.lower() == path:
                path=i

        text_to_speech('If I am correct then you want create {} under {}'.format(dir_name , path))
        reply = recognize_speech()
        if reply  in ['yes','yo','yep','yup']:
            try:
                sr.os.system('mkdir /home/pybot/{}/{}'.format(path,dir_name))
            except:

                text_to_speech('Something went wrong')


            text_to_speech('Job done')
        else:
            pass








    elif 'remove' in usr_input or 'delete' in usr_input:
        pass
    else:
        pass


# print(text)






# for i in dir(obj):
#     print(i)


