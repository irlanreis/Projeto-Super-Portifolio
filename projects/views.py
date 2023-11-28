from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificateSerializer,
    CertifyingInstitutionSerializer,
)
from .models import Profile, Project, Certificate, CertifyingInstitution

from rest_framework.permissions import AllowAny, IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrive(self, request, *args, **kwargs):
        if self.request.method == "GET":
            profile_id = self.kwargs["pk"]
            profile = Profile.objects.get(id=profile_id)
            context = {
                "profile": profile,
                "projects": profile.project_set.all(),
                "certificates": profile.certificate_set.all(),
            }

            return render(request, "profile_detail.html", context)

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
