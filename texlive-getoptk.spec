# revision 23567
# category Package
# catalog-ctan /macros/plain/contrib/getoptk
# catalog-date 2011-08-07 22:43:01 +0200
# catalog-license nosource
# catalog-version 1.0
Name:		texlive-getoptk
Version:	1.0
Release:	11
Summary:	Define macros with sophisticated options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/getoptk
License:	NOSOURCE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getoptk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/getoptk.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of defining macros whose options
are taken from a dictionary, which includes options which
themselves have arguments. The package was designed for use
with Plain TeX; its syntax derives from that of the \hbox,
\hrule, etc., TeX primitives.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/getoptk/getoptk.tex
%{_texmfdistdir}/tex/plain/getoptk/guide.tex
%doc %{_texmfdistdir}/doc/plain/getoptk/COPYING
%doc %{_texmfdistdir}/doc/plain/getoptk/COPYING-FR
%doc %{_texmfdistdir}/doc/plain/getoptk/README
%doc %{_texmfdistdir}/doc/plain/getoptk/guide.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 752265
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718541
- texlive-getoptk
- texlive-getoptk
- texlive-getoptk
- texlive-getoptk

