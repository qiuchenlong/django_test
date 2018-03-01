from django.shortcuts import render, render_to_response

# Create your views here.

import json
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.http import require_http_methods

from polls.models import Person#, User, Project

import csv


from reportlab.pdfgen import canvas

from django.shortcuts import render



class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value



@require_http_methods(["GET"])
def index(request, arg):
    # p = Person(first_name="Q...", last_name="chenlong", p_money=10000)
    # p.save()

    print("arg", arg)

    if request.method == 'GET':
        # id = request.GET.get("id", "")
        # print(id)
        # resp = dict(
        #     id=id
        # )
        # # return HttpResponse("ok")
        # return HttpResponse(json.dumps(resp), content_type="application/json")


        # import datetime
        # now = datetime.datetime.now()
        # html = "<html><body>It is now %s.</body></html>" % now
        # return HttpResponse(html)

        # return FileResponse(open("static/1.jpg", "rb"))


        # resp = HttpResponse(content_type="text/csv")
        # resp['Content-Disposition'] = 'attachment; filename="somefilename.csv"' # save of filename
        #
        # writer = csv.writer(resp)
        # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
        #
        # return resp

        # rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
        # pseudo_buffer = Echo()
        # writer = csv.writer(pseudo_buffer)
        # response = StreamingHttpResponse((writer.writerow(row) for row in rows),
        #                                  content_type="text/csv")
        # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        # return response

        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        #
        # # Create the PDF object, using the response object as its "file."
        # p = canvas.Canvas(response)
        #
        # # Draw things on the PDF. Here's where the PDF generation happens.
        # # See the ReportLab documentation for the full list of functionality.
        # p.drawString(100, 100, "Hello world.")
        #
        # # Close the PDF object cleanly, and we're done.
        # p.showPage()
        # p.save()
        # return response


        # return HttpResponse("lee")
        # return render(request, "test.html", {"hello": "world..."})


        person = Person.objects.all().filter(first_name="Q...")
        print(person)

        person = Person.objects.get(last_name="")
        print(person.first_name, person.last_name, person.p_money)

        Person.objects.filter(last_name="").update(p_money="56515")

        ps = Person.objects.all()#.filter(p_money=10001)
        print(len(ps))

        return HttpResponse("lee")

        # ps1 = User.objects.all()[5:15]
        # ps2 = User.objects.all()[5:15:4]
        # for i in range(len(ps1)):
        #     print(ps1[i].username, ps1[i].phone)
        #
        # resp = [x.username for x in ps2]
        #
        # # resp = User.objects.order_by('phone')[0]
        # # return HttpResponse(json.dumps(resp), content_type="application/json")
        #
        # # obj = User.objects.all()
        # obj = Project.objects.all()[:10]
        # return render(request, "index.html", locals())


from polls.forms import FileUploadForm

def upload_file(request):
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            f = my_form.cleaned_data['my_file']
            handle_uploaded_file(f)
        return HttpResponse('Upload Success')
    else:
        my_form = FileUploadForm()
    return render(request, 'upload_temp.html', {'form': my_form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


from django.urls import reverse
from django.http import HttpResponseRedirect

def test(request, year='2008'):
    id = request.GET.get("id")
    # return HttpResponse('hello...%s...%s' % (id, year))
    # return render(request, 'test.html', {'hello': id})
    # return render(request, reverse('test', args=(id,)))
    # tmp = reverse('test', )
    # return HttpResponseRedirect(reverse('test', args=(id,)))
    # return HttpResponseRedirect(tmp)
    return render(request, 'test.html')

def testx(request, year='2008'):
    id = request.GET.get("id")
    # a = 1/0
    # return HttpResponse('hello...%s...%s' % (id, year))
    # return render(request, 'test.html', {'hello': id})
    # return render(request, reverse('test', args=(id,)))
    # tmp = reverse('test', )
    # return HttpResponseRedirect(reverse('test', args=(id,)))
    # return HttpResponseRedirect(tmp)
    return render(request, 'test.html', {'year': year})


from django.template import RequestContext

def error_404(request):
    print(404)
    response = render_to_response('error_404.html', {},
                                  RequestContext(request))
    response.status_code = 404
    return response
    # return render(request, 'error_404.html')

def error_500(request):
    print(500)
    response = render_to_response('error_500.html', {},
                                  RequestContext(request))
    response.status_code = 500
    return response



# from django.dispatch import receiver
# from django.core.signals import request_started, request_finished, got_request_exception
#
# @receiver(request_started)
# def my_callback1(sender, **kwargs):
#     print(sender)
#     print(kwargs)
#     print("Request started!")
#
# @receiver(request_finished)
# def my_callback2(sender, **kwargs):
#     print(sender)
#     print(kwargs)
#     print("Request finished!")
#
# @receiver(got_request_exception)
# def my_callback3(sender, **kwargs):
#     print(sender)
#     print(kwargs)
#     print("Request exception!")

# from django.core.signals import request_finished
# request_finished.connect(my_callback)
