Name:		texlive-bmstu
Version:	65897
Release:	1
Summary:	A LaTeX class for Bauman Moscow State Technical University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bmstu
License:	lppl1.3 other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class defines commands and environments for creating
reports and explanatory notes in Bauman Moscow State Technical
University (Russia). Klass opredeliaet komandy i okruzheniia
dlia sozdaniia otchetov i raschetno-poiasnitel'nykh zapisok v
MGTU im. N. E. Baumana. Sgenerirovannye faily sootvetstvuiut
trebovaniiam MGTU im. N. E. Baumanai GOST 7.32-2017.
Raschetno-poiasnitel'nye zapiski k vypusknym kvalifikatsionnym
rabotam uspeshno prokhodiat proverku TestVKR (sborka 203).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bmstu
%doc %{_texmfdistdir}/doc/latex/bmstu

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
