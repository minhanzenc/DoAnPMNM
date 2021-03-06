# Generated by Django 3.2.9 on 2021-11-01 14:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanhMucSanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_danh_muc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tong_tien', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('ngay_tao', models.DateTimeField(auto_now=True)),
                ('tinh_trang', models.IntegerField(choices=[(1, 'don hang dang cho'), (2, 'don hàng dang giao'), (3, 'don hang thanh cong '), (4, 'don hang that bai ')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiSanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_loai', models.CharField(max_length=100)),
                ('danh_muc_san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.danhmucsanpham')),
            ],
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('so_dien_thoai', models.CharField(max_length=11)),
                ('dia_chi', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_san_pham', models.CharField(max_length=100)),
                ('gia', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('gioi_thieu', models.TextField()),
                ('loai_san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.loaisanpham')),
            ],
        ),
        migrations.CreateModel(
            name='KhuyenMai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gia_giam', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('ngay_ap_dung', models.DateTimeField(blank=True, null=True)),
                ('ngay_ket_thuc', models.DateTimeField()),
                ('don_hang', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClothApp.donhang')),
            ],
        ),
        migrations.AddField(
            model_name='donhang',
            name='khach_hang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChiTietSanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.IntegerField()),
                ('size', models.CharField(choices=[('S', 'Nho'), ('M', 'Vua'), ('L', 'Lon'), ('XL', 'Sieu Lon')], default='S', max_length=2)),
                ('mau_sac', models.CharField(max_length=50)),
                ('hinh', models.ImageField(upload_to='static/hinh/sanpham')),
                ('san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.sanpham')),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietDonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.IntegerField()),
                ('chi_tiet_san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.chitietsanpham')),
                ('don_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.donhang')),
            ],
        ),
    ]
