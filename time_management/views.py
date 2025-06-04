from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import TimeForm
from .models import Time
from django.utils import timezone


def home(request):
    if not request.user.is_authenticated:
        return redirect('log_in')
    else:
        today = timezone.now().date()
        entries = Time.objects.filter(user=request.user.id, date=today)

        totals = {
            'console': sum(i.console_time for i in entries),
            'computer': sum(i.computer_time for i in entries),
            'mobile': sum(i.mobile_time for i in entries),
            'television': sum(i.television_time for i in entries),
        }

        context = {
            "time": today,

            "console_hours": totals["console"] // 60,
            "console_minutes": totals["console"] % 60,

            "computer_hours": totals["computer"] // 60,
            "computer_minutes": totals["computer"] % 60,

            "mobile_hours": totals["mobile"] // 60,
            "mobile_minutes": totals["mobile"] % 60,

            "television_hours": totals["television"] // 60,
            "television_minutes": totals["television"] % 60
        }

        if request.method == "POST":
            form = TimeForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user.id
                obj.save()
                messages.success(request, "Your data was successfully recorded.")
                return redirect("time_management:home")
        else:
            form = TimeForm()
            context["form"] = form
        return render(request, "home.html", context)

