from django.http import StreamingHttpResponse, HttpResponse, JsonResponse, HttpResponseBadRequest
from requests import session
from v_stream.camera import VideoCamera, getDistance
from django.shortcuts import render
from datetime import datetime
from v_stream.models import Measurements, Session, ModelInfo, MeasureTemp
# from v_stream.models import MeasurementsForm
# from v_stream.camera import GreyVideoCamera
# from v_stream.camera import BinaryVideoCamera
import json
import cv2
import threading



def home(request):
    return render(request, 'v_stream/home.html')

def about(request):
    return render(request, 'v_stream/about.html')

def contact(request):
    return render(request, 'v_stream/contact.html')

def tour(request):
    return render(request, 'v_stream/tour.html')

def features(request):
    return render(request, 'v_stream/features.html')

def history(request):
    return render(request, 'v_stream/history.html')

def zoom(request):
    return render(request, 'v_stream/zoom.html')

def model(request):
    return render(request, 'v_stream/model.html')

def form(request):
    now = datetime.now()
    session_id = now.strftime("%d%m%Y%H%M%S")
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    return render(request, 'v_stream/form.html', {'session_id': session_id, 'date': date, 'time':time})

def stream(request):
    return render(request, 'v_stream/stream.html')

def sbinary(request):
    return render(request, 'v_stream/sbinary.html')

def sgray(request):
    return render(request, 'v_stream/sgray.html')

def click(event, x,y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x,y)
        point = (x,y)

def gen(camera):
    while True:
        frame = camera.get_frame()

        # cv2.setMouseCallback(frame, click)
        yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type ="multipart/x-mixed-replace;boundary=frame")

# def grey_scale(request):
#     return StreamingHttpResponse(gen(GreyVideoCamera()),
#                                  content_type='multipart/x-mixed-replace; boundary=frame')

# def binary_scale(request):
#     return StreamingHttpResponse(gen(BinaryVideoCamera()),
#                                  content_type='multipart/x-mixed-replace; boundary=frame')


def Insertmodel(request):   #Model Registraion
    if request.method=='POST':
        if request.POST.get('model_id') and request.POST.get('cloth_type') and request.POST.get('sh_width') and request.POST.get('width')and request.POST.get('length')  and request.POST.get('c_rgb')and request.POST.get('c_html') :

            model_id = request.POST.get('model_id')
            cloth_type = request.POST.get('cloth_type')
            sh_width = request.POST.get('sh_width')
            chest = request.POST.get('chest')
            width = request.POST.get('width')
            length = request.POST.get('length')
            nk_width = request.POST.get('nk_width')
            sl_length = request.POST.get('sl_length')
            c_rgb = request.POST.get('c_rgb')
            c_html = request.POST.get('c_html')



            updated_values = {

                'cloth_type': cloth_type,
                'sh_width': sh_width,
                'chest':chest,
                'width': width,
                'length': length,
                'nk_width':nk_width,
                'sl_length':sl_length,
                'c_rgb':c_rgb,
                'c_html': c_html
                }

            obj, created = ModelInfo.objects.update_or_create(
            model_id=model_id,
            defaults=updated_values
            )

            now = datetime.now()
            session_id = now.strftime("%d%m%Y%H%M%S")
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")


            return render(request, 'v_stream/form.html', {
                'session_id': session_id,
                'date': date,
                'time':time,
                'model_id':model_id,

                })

    else:
        return render(request, 'v_stream/model.html')



def Insertrecord(request):   #Session Registraion 
    if request.method=='POST':
        if request.POST.get('session_id') and request.POST.get('model_id') and request.POST.get('date') and request.POST.get('time')and request.POST.get('invest_id')  and request.POST.get('investigator')and request.POST.get('country') :

            session_id = request.POST.get('session_id')
            model_id = request.POST.get('model_id')
            date = request.POST.get('date')
            time = request.POST.get('time')
            invest_id = request.POST.get('invest_id')
            investigator = request.POST.get('investigator')
            country = request.POST.get('country')


            saverecord = Session()
            saverecord.session_id=session_id
            saverecord.model_id=model_id
            saverecord.date=date
            saverecord.time=time
            saverecord.invest_id=invest_id
            saverecord.investigator=investigator
            saverecord.country=country
            saverecord.save()

            model = ModelInfo.objects.get(model_id=model_id)


            return render(request, 'v_stream/stream.html' , {
                'session_id': session_id,
                'model_id': model_id,
                'date': date,
                'time': time,
                'invest_id': invest_id,
                'investigator': investigator,
                'country': country,
                'cloth_type': model.cloth_type,
                'sh_width': model.sh_width,
                'chest':model.chest,
                'length': model.length,
                'width': model.width,
                'sl_length': model.sl_length,
                'nk_width': model.nk_width,
                'c_rgb':model.c_rgb,
                'c_html': model.c_html

            })
    else:
        return render(request, 'v_stream/form.html')



def Tempmeasure(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
           
            
            data = json.load(request)
            x1 = data.get('X1')
            x2 = data.get('X2')
            y1 = data.get('Y1')
            y2 = data.get('Y2')
            # place =data.grt('place')
            
            distance = getDistance(x1,y1,x2,y2)

            # saverecord = MeasureTemp()
            # saverecord.click_id=click_id
            # saverecord.X1=x1
            # saverecord.Y1=y1
            # saverecord.X2=x2
            # saverecord.Y2=y2
            # saverecord.save()
            

            return JsonResponse({'status': 'success', 'distance': distance})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')



def InsertMeasure(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            now = datetime.now()
            measure_id = now.strftime("M" + "%d%m%Y%H%M%S")  # measurement id is load from current time
            
            data = json.load(request)
            session_id = data.get('session_id')
            x1 = data.get('X1')
            x2 = data.get('X2')
            y1 = data.get('Y1')
            y2 = data.get('Y2')
            place =data.get('place')
            distance = data.get('distance')
        
           
            

            saverecord = Measurements()
            saverecord.measure_id=measure_id
            saverecord.session_id=session_id
            saverecord.X1=x1
            saverecord.Y1=y1
            saverecord.X2=x2
            saverecord.Y2=y2
            saverecord.distance=distance
            saverecord.place=place
            saverecord.save()

            
          
            
            # model = Session.objects.get(session_id=session_id)
            # return render(request, 'v_stream/stream.html' , {
            #     'session_id': session_id,
                
            # })

            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

    
    



