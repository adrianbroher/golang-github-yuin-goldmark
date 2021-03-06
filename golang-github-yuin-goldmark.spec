# Generated by go2rpm 1
%bcond_without check

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.1.21

%gometa

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Jan 25 15:34:31 CET 2020 Marcel Metz <mmetz@adrian-broher.net> - 1.1.21-1
- Initial package
