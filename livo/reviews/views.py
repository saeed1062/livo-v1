from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reviews.models import Review
from users.models import User

@login_required
def add_review(request):
    if request.method == 'POST':
        reviewed_user_id = request.POST.get('reviewed_user_id')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if reviewed_user_id and rating and comment:
            reviewed_user = get_object_or_404(User, id=reviewed_user_id)
            
            # Prevent self review
            if reviewed_user == request.user:
                messages.error(request, "You cannot review yourself.")
            else:
                try:
                    Review.objects.create(
                        reviewer=request.user,
                        reviewed_user=reviewed_user,
                        rating=int(rating),
                        comment=comment
                    )
                    messages.success(request, f"Review for {reviewed_user.get_full_name() or reviewed_user.username} submitted successfully!")
                except Exception as e:
                    messages.error(request, f"Error saving review: {str(e)}")
        else:
            messages.error(request, "Please provide rating and comment.")
            
        # Redirect back to where they came from
        return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
        
    return redirect('dashboard')

