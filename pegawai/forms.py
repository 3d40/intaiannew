from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormTpegawaiSapk(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['nip_baru','nama', 'gelar_depan', 'gelar_blk', 'gol', 'tmt_golongan', 'tgl_lhr', 'jenis_kelamin','nik', 'nomor_hp', 'email', 'alamat', 'jenis_pegawai', 'jabatan','unor', 'unor_induk']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OpdForm(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = ['unor_induk_bkd']

class ProfileSearchForm(forms.Form):
    nama = forms.CharField(required=False)

class FormTRiwayatGolongan(ModelForm):
    class Meta:
        model = TRiwayatGolongan
        fields = ['jenis_kp', 'id_golongan', 'sk_nomor', 'sk_tanggal','tmt_golongan','mk_golongan_tahun', 'mk_golongan_bulan', 'dokumen']