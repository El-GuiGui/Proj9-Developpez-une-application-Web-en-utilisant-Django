from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserFollows
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse


@login_required
def subscribe(request):
    followed_users = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        query = request.GET.get("term", "")
        users = (
            User.objects.filter(username__icontains=query)
            .exclude(username=request.user.username)
            .exclude(id__in=followed_users.values_list("followed_user_id", flat=True))
            .exclude(username="admin")
        )
        results = [user.username for user in users]
        return JsonResponse(results, safe=False)

    if request.method == "POST":
        if "user_to_follow" in request.POST:
            username_to_follow = request.POST.get("user_to_follow")
            if username_to_follow:
                try:
                    user_to_follow = User.objects.get(username=username_to_follow)
                    if request.user != user_to_follow:
                        _, created = UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
                        if created:
                            messages.success(request, f"Vous suivez maintenant {user_to_follow.username}.")
                        else:
                            messages.info(request, "Vous suivez déjà cet utilisateur.")
                    else:
                        messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
                except User.DoesNotExist:
                    messages.error(request, "Aucun utilisateur trouvé avec ce nom d'utilisateur.")

        elif "unfollow_user_id" in request.POST:
            user_id_to_unfollow = request.POST.get("unfollow_user_id")
            if user_id_to_unfollow:
                user_to_unfollow = get_object_or_404(User, pk=user_id_to_unfollow)
                UserFollows.objects.filter(user=request.user, followed_user=user_to_unfollow).delete()
                messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")

        return redirect("subscribe")

    return render(request, "subscriptions/subscribe.html", {"followed_users": followed_users, "followers": followers})
