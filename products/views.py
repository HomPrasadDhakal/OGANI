from django.shortcuts import render

# VIEWS FOR ADMIN PANNEL
def AdminDashBoardView(request):
    template="admin/index.html"
    context = {}
    return render(request, template, context)
