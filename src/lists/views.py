from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List

def home_page(request):
    return render(request, "home.html")

def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    error = None

    if request.method == "POST":
        item = Item.objects.create(text=request.POST["item_text"], list=our_list)
        try:
            item.full_clean()
            item.save()
            return redirect(f"/lists/{our_list.id}/")
        except ValidationError:
            item.delete()
            error = "You can't have an empty list item"

    return render(request, "list.html", {"list": our_list, "error": error})

def new_list(request):
    nulist = List.objects.create()
    item = Item.objects.create(text=request.POST["item_text"], list=nulist)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        nulist.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    return redirect(f"/lists/{nulist.id}/")