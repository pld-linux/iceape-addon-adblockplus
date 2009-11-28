%define		realname	adblock_plus
Summary:	Extension for blocking unwanted ads, banners etc.
Summary(pl.UTF-8):	Rozszerzenie do blokowania niechcianych reklam, bannerów itp.
Name:		iceape-addon-adblockplus
Version:	1.1.1
Release:	1
Epoch:		1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/addons/1865/%{realname}-%{version}-fx+sm+tb.xpi
# Source0-md5:	6ea1304754d1d4ebbc4558d9c73fec18
URL:		http://adblockplus.org/
BuildRequires:	unzip
Requires(post,postun):	iceape >= 2.0
Requires:	iceape >= 2.0
Obsoletes:	seamonkey-addon-adblockplus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ever been annoyed by all those ads and banners on the internet that
often take longer to download than everything else on the page?
Adblock Plus will help you to get rid of them. Right-click on a banner
and choose "Adblock" from the context menu - the banner won't be
downloaded again. Or open Adblock Plus sidebar to see all elements of
the page and block the banners. You can use filters with wildcards or
even regular expressions to block complete banner factories.

%description -l pl.UTF-8
Czy denerwują Cię te wszystkie reklamy i bannery, których załadowanie
często trwa dłużej niż wczytanie właściwej treści strony? Adblock Plus
pomoże Ci się ich pozbyć. Kliknij prawym przyciskiem myszki na
bannerze i wybierz "Adblock" z menu kontekstowego - banner już więcej
się nie wyświetli. Możesz też otworzyć panel Adblock Plus aby zobaczyć
listę wszystkich elementów strony i zablokować bannery. Możliwe
również jest tworzenie filtrów używających masek lub nawet wyrażeń
regularnych aby umożliwić blokowanie całych serwisów reklamowych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/iceape
install -d $RPM_BUILD_ROOT%{_libdir}/iceape

unzip %{SOURCE0} -d $RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT/chrome
mv $RPM_BUILD_ROOT/chrome.manifest $RPM_BUILD_ROOT/chrome/adblockplus-installed-chrome.txt
mv $RPM_BUILD_ROOT/defaults/preferences $RPM_BUILD_ROOT/defaults/pref
mv $RPM_BUILD_ROOT/{chrome,defaults} $RPM_BUILD_ROOT%{_datadir}/iceape
mv $RPM_BUILD_ROOT/components $RPM_BUILD_ROOT%{_libdir}/iceape

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/iceape-chrome+xpcom-generate

%postun
%{_sbindir}/iceape-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_datadir}/iceape/chrome/adblockplus.jar
%{_datadir}/iceape/chrome/adblockplus-installed-chrome.txt
%{_datadir}/iceape/defaults/pref/adblockplus.js
%{_libdir}/iceape/components/AdblockPlus.*
