Summary:	2D platform action game
Summary(pl.UTF-8):	Dwuwymiarowa platformowa gra akcji
Name:		blobwars
Version:	1.14
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
# download it from http://parallelrealities.co.uk/projects/blobWars.php
# and put it into the blobwars dir
Source0:	%{name}-%{version}-1.tar.gz
# Source0-md5:	c4133a08d49d63b518e70d67b88fb8be
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://parallelrealities.co.uk/projects/blobWars.php
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Episode I of the Blob Wars Saga.

The aim of the game is to go through the levels and rescue as many
MIAs as you can. The missions also contain other objectives, some
optional.

%description -l pl.UTF-8
Jest to pierwszy Epizod Sagi Blob Wars.

Celem gry jest pokonywanie kolejnych poziomów i uratowanie tak wielu
MIA jak to możliwe. Misje zawierają również inne zadania,
niektóre opcjonalne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc
%attr(755,root,root) %{_bindir}/blobwars
%dir %{_datadir}/%{name}
%{_datadir}/blobwars/blobwars.pak
%{_desktopdir}/blobwars.desktop
%{_iconsdir}/hicolor/*/apps/blobwars.png
