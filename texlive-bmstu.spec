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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bmstu
%dir %{_datadir}/texmf-dist/tex/latex/bmstu
%dir %{_datadir}/texmf-dist/doc/latex/bmstu/examples
%dir %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc
%dir %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc/img
%dir %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc/lst
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/examples/bmstu-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/examples/bmstu-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc/img/tux.png
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc/img/tuz.png
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/examples/inc/lst/main.c
%doc %{_datadir}/texmf-dist/doc/latex/bmstu/manifest.txt
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-appendix.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-biblio.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-defabbr.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-essay.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-figure.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-listing.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-logo.pdf
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-title.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu-toc.sty
%{_datadir}/texmf-dist/tex/latex/bmstu/bmstu.cls
