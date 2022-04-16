Name: hmcl
Version: 3.5.2.218
Release:        1%{?dist}
Summary:play minecraft on Fedora

License: GPLv3+
URL:https://hmcl.huangyuhui.net/
Source0:hmcl
Source1:hmcl.jar
source2:hmcl.png
source3:hmcl.desktop

AutoReqProv: no
Requires: java-17 javafx

%description
play Minecraft on Fedora!!

%prep

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/hmcl/
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icon

install -D -m 777 %{SOURCE0} %{buildroot}/usr/bin
install -D  %{SOURCE1} %{buildroot}/usr/share/hmcl

cp %{SOURCE2}  %{buildroot}/usr/share/icon
cp %{SOURCE3}  %{buildroot}/usr/share/applications
rm -rf  %{_builddir}/*



%files
/usr/bin/hmcl
/usr/share/applications/hmcl.desktop
/usr/share/icon/hmcl.png
/usr/share/hmcl


%changelog

