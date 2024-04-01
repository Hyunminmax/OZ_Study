from django.contrib import admin
from .models        import Board

# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    # pass
    # 아래 값은 튜플이나 리스트로 대입가능
    list_display = ('title', 'content', 'author', 'date', 'updated_at', 'created_at')
    # 단일 튜플은 끝에 ','를 사용해야 함.
    list_filter = ('date',)
    search_fields = ('author', 'content')
    ordering = ('date',)
    readonly_fields = ('author',)
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        # 'Advanced options'은 변경 가능
        # ('Advanced options', {'fields': ('author', 'likes', 'reviews'), 'classes': ('collapse',)}),
        ('Here are options', {'fields': ('author', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )
    
    actions = ('increment_likes', )

    # 예시에서는 request사용안함. 
    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"
