from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reviews.models import Ticket
from .forms import TicketForm


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            try:
                ticket.save()
                print("Ticket enregistré avec succès : ", ticket)
                return redirect("flux")
            except Exception as e:
                print("Erreur lors de l'enregistrement du ticket : ", e)
        else:
            print("Formulaire non valide : ", form.errors)
    else:
        form = TicketForm()
    return render(request, "tickets/create_ticket.html", {"form": form})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = TicketForm(instance=ticket)
    return render(request, "tickets/edit_ticket.html", {"form": form, "ticket": ticket})
