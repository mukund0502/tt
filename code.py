from pyVoIP.VoIP import VoIPPhone, InvalidStateError, VoIPCall, CallState
import pyaudio
import numpy as np 
import wave
import io
import soundfile as sf
VoIPCall.state == CallState.ANSWERED


def answer(call): 
    try:
        call.answer()
        audio_file = []
        while (call.state == CallState.ANSWERED):
            audio = call.read_audio(length = 160, blocking = True)
            audio_file.append(audio)
        
        combined_audio = np.concatenate(audio_file)
        data, samplerate = sf.read(io.BytesIO(combined_audio))
        """src = https://stackoverflow.com/questions/52369925/creating-wav-file-from-bytes """
        print(samplerate)
        print(data.shape)

        call.hangup()
    except InvalidStateError:
        pass
  

sip_server_ip = ""
sip_server_port = 0
sip_server_username = ""
sip_server_password = ""
computer_ip = ""
sip_port = 5060

""" src = """

if __name__ == "__main__":
    phone=VoIPPhone(sip_server_ip, sip_server_port, sip_server_username, sip_server_password, callCallback=answer, myIP=computer_ip, sipPort=sip_port , rtpPortLow=10000, rtpPortHigh=20000)
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()
