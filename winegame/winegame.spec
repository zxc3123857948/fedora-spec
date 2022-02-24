Name: net.winegame.client
Version: 0.5.9.3
Release: 1
Summary: winegame
License: None
URL:  https://winegame.net/
Packager: llozi
Source0: net.winegame.client_%{version}_amd64.deb
Requires:  python-gobject python3-pyyaml python-evdev  python-pillow  python-requests  python-dbus  python-distro  gtk3 glib2 psmisc cabextract unzip  p7zip  tar  curl  wget aria2 libXrandr  zenity mesa-demos wine  vulkan-loader    vulkan-loader(x86-32)   vulkan-tools python3-lxml  python3-giacpy python3-setproctitle  python3-file-magic  xorg-x11-xfs-utils collectd-notify_desktop glx-utils python3-distro  fluid-soundfont-gs winetricks  gamemode

%description

%prep
ar x %{SOURCE0}
tar -xf data.tar.xz
%install
mkdir -p %{buildroot}
cp -R ~/rpmbuild/BUILD/opt %{buildroot}
cp -R ~/rpmbuild/BUILD/usr %{buildroot}
rm -rf %{buildrot}/opt/apps/net.winegame.client/files/
%pre

%post

%preun

%postun

%files
/usr/share/
/opt/apps/net.winegame.client/






