%global tl_name bmstu
%global tl_revision 65897

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.0
Release:	%{tl_revision}.1
Summary:	A LaTeX class for Bauman Moscow State Technical University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bmstu
License:	lppl1.3 other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bmstu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class defines commands and environments for creating reports and
explanatory notes in Bauman Moscow State Technical University (Russia).
Klass opredeliaet komandy i okruzheniia dlia sozdaniia otchetov i
raschetno-poiasnitel'nykh zapisok v MGTU im. N. E. Baumana.
Sgenerirovannye faily sootvetstvuiut trebovaniiam MGTU im. N. E.
Baumanai GOST 7.32-2017. Raschetno-poiasnitel'nye zapiski k vypusknym
kvalifikatsionnym rabotam uspeshno prokhodiat proverku TestVKR (sborka
203).

