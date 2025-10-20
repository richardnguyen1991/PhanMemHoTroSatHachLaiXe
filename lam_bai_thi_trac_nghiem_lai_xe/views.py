from django.http import HttpResponse


def trang_chu(request):
    """Trang chào mừng đơn giản cho ứng dụng làm bài thi trắc nghiệm."""

    return HttpResponse("Chào mừng đến với ứng dụng làm bài thi trắc nghiệm lái xe!")
