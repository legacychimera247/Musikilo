Name:       musikilo

Summary:    Music player
Version:    2.0.0
Release:    1
Group:      Qt/Qt
License:    GPLv3
URL:        http://verdanditeam.com/
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   libqofonoext-declarative
Obsoletes:  harbour-musikilo < 2.0.0
BuildRequires: pkgconfig(sailfishapp) >= 1.0.2
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5WebSockets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: desktop-file-utils

%description
Music player

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
rm -rf %{buildroot}/usr/include/ %{buildroot}/usr/lib/ %{buildroot}/usr/lib64/ %{buildroot}/usr/share/qt5/ %{buildroot}/usr/share/smpc/ \
    %{buildroot}/usr/share/icons/hicolor/86x86/apps/smpc.png %{buildroot}/usr/bin/libsmpc.a

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
