from django.shortcuts import render


def Index(request):
    return render(request, 'index.html')


def Movies(request):
    my_dict = {
        'Heading_msg': 'Movies Information',
        'Sub_msg1': 'Sonali Slowly Getting Cured.',
        'Sub_msg2': 'Bahubali-4 Is Just Planning',
        'Sub_msg3': 'Salman Khan Is Married Soon'
    }
    return render(request, 'news.html', context=my_dict)
    

def Sports(request):
    my_dict = {
        'Heading_msg': 'Sports Information',
        'Sub_msg1': 'Sonali Slowly Getting Cured.',
        'Sub_msg2': 'Bahubali-4 Is Just Planning',
        'Sub_msg3': 'Salman Khan Is Married Soon'
    }
    return render(request, 'news.html', context=my_dict)



def Politics(request):
    my_dict = {
        'Heading_msg': 'Politics Information',
        'Sub_msg1': 'Sonali Slowly Getting Cured.',
        'Sub_msg2': 'Bahubali-4 Is Just Planning',
        'Sub_msg3': 'Salman Khan Is Married Soon'
    }
    return render(request, 'news.html', context=my_dict)

