Summary: A graphical interface for modifying the system language
Name: system-config-language
Version: 1.3.4
Release: 5%{?dist}
URL: https://fedorahosted.org/system-config-language/
Source0: https://fedorahosted.org/releases/s/y/system-config-language/%{name}-%{version}.tar.bz2
License: GPLv2
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
Requires: pygtk2
Requires: python2
Requires: usermode >= 1.36
Requires: usermode-gtk >= 1.36
Requires: yum >= 2.9.5
Requires: gtk2 >= 2.6
Obsoletes: locale_config  <= %{version}
Patch1: bug-589171.patch
Patch2: bug-607250.patch
Patch3: bug-619267.patch
Patch4: bug-619261.patch
Patch5: bug-622412.patch

%description
system-config-language is a graphical user interface that 
allows the user to change the default language of the system.

%prep
%setup -q
%patch1 -p1 -b .1-translation-patch
%patch2 -p1 -b .1-fixed-gui-heigth-for-low-resolution
%patch3 -p1 -b .1-corrected-locale-name-for-sr
%patch4 -p1 -b .1-handlnig-comps-group
%patch5 -p1 -b .1-handling-@scriptname

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make INSTROOT=$RPM_BUILD_ROOT install
install $RPM_BUILD_DIR/system-config-language-%{version}/yumhelpers.glade $RPM_BUILD_ROOT%{_datadir}/system-config-language

chmod 0644 $RPM_BUILD_ROOT%{_datadir}/system-config-language/*.py* 
chmod 0755 $RPM_BUILD_ROOT%{_datadir}/system-config-language/language_gui.py
chmod 0755 $RPM_BUILD_ROOT%{_datadir}/system-config-language/language_backend.py
chmod 0755 $RPM_BUILD_ROOT%{_datadir}/system-config-language/system-config-language.py
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/system-config-language/yumhelpers.glade
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/system-config-language
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/system-config-language
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/system-config-language/pixmaps/system-config-language.png
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/system-config-language.png
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/system-config-language/locale-list


desktop-file-install --vendor system --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category System \
  --add-category Settings \
  --add-category X-Red-Hat-Base                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/system-config-language.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING
#%doc doc/*
%{_bindir}/system-config-language
%dir %{_datadir}/system-config-language
%{_datadir}/system-config-language/*
#%dir %{_datadir}/firstboot/
#%dir %{_datadir}/firstboot/modules
#%{_datadir}/firstboot/modules/language.py*
%{_datadir}/applications/system-config-language.desktop
%{_datadir}/icons/hicolor/48x48/apps/system-config-language.png
%config(noreplace) %{_sysconfdir}/pam.d/system-config-language
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-language

%changelog
* Wed Aug 11 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-5
- Resolves: bug 622412

* Wed Aug 04 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-4
- Resolves: bug 619267
- Resolves: bug 619261

* Fri Jul 30 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-3
- Resolves: bug 607250

* Mon May 10 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-2
- Resolves: bug 589171

* Fri Mar 12 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-1
- upstrem new release with updated translations 
- Resolves: bug 572823

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.3-6
- Resolves: bug 568654

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.3-5
- Resolves: bug 568286

* Thu Dec 10 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-4
- updated URL and source field

* Mon Oct 26 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-3
- fixed 530698

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-2
- fixed 525040

* Wed Sep 23 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-1
- upstream release of 1.3.3
- updated .pot files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 24 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-9
- fix bug 493888

* Mon Jul 13 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-8
- fix bug 493858, 507796

* Tue Jul 07 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-7
- fix bug 598975
- patch from Jeremy Katz katzj@redhat.com

* Mon May 25 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-6
- fix bug 493824

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.2-4
- Rebuild for Python 2.6

* Wed Oct 22 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-3
- fix bug 467919

* Wed Oct 8 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-2
- fix bug 462914

* Wed Sep 17 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-1
- upstream realease 1.3.2
- fix bug 444568, 462439

* Wed Jul 16 2008 Pravin Satpute <psatpute@redhat.com> - 1.3.1-2
- fix bug 442901

* Tue Jun 24 2008 Pravin Satpute <psatpute@redhat.com> - 1.3.1-1
- upstream release 1.3.1

* Mon May 26 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-5
- modified system-config-language-447008.patch file

* Thu May 22 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-4
- fix bug 447008
- fix bug 429808
- fix bug 447879

* Mon Apr 28 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-3
- fix bug 442901

* Tue Jan 15 2008 Lingning Zhang <lizhang@redhat.com> - 1.2.15-2
- fix bug428391.

* Wed Dec 26 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.15-1
- fix bug294561.

* Tue Nov 27 2007 Parag Nemade <pnemade@redhat.com> - 1.2.14-2
- Merge review SPEC cleanup rh#226461

* Mon Nov 19 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.14
- fix bug386731.

* Mon Oct 22 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.13
- fix bug332361.

* Tue Oct 9 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.12
- fix bug294531.

* Fri Sep 21 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.11
- fix bug294571.

* Thu Sep 20 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.10
- fix bug288851 and bug297461.
- add the Nepali support.

* Mon Sep 10 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.9
- fix bug275711 and bug284331.

* Mon Aug 20 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.8
- re-fix bug251478.

* Mon Aug 13 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.7
- fix bug251478.

* Mon Aug 6 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.6
- re-fix bug241744.

* Thu Jul 5 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.5
- fix bug241746.

* Tue Jul 3 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.4
- fix bug241747 and bug246578.

* Tue Jul 3 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.3
- fix bug245872 and bug241744.

* Tue Jun 19 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.2
- modify the category value in system-config-language.spec.
- fix bug243529. 

* Mon Jun 18 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.1
- Fix bug237715, bug241744 and bug225949(patch from Stephanos Manos).

* Tue May 29 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.0
- support to install languages what is not installed.

* Fri May 25 2007 Lingning Zhang <lizhang@redhat.com> - 1.1.18-1
- Update translations (#216093)
- Add new languages (#217125, #239999)

* Wed Nov 22 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.16-1
- Update translations (#216093)

* Thu Nov 16 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.15-1
- Use correct Norwegian language (#209438)
- Fix traceback in text mode (#215319)
- Update potfile

* Fri Oct 20 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.14-1
- Fix typos (#211434)

* Mon Oct 16 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.13-1
- Fix Chinese locale re-selection (#208407)

* Fri Oct 13 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.12-1
- Add Orya support (#210373)

* Mon Jul 17 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.11-2
- Don't nuke *.pyc in preun (#198959)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.11-1.1
- rebuild

* Tue Feb 28 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.11-1
- Update translations
- Serbian locales (#172600)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 24 2005 Paul Nasrat <pnasrat@redhat.com> - 1.1.10-1
- pam_stack deprecated (#170631)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1.1.9-2
- silence %%post

* Fri Apr 01 2005 Paul Nasrat <pnasrat@redhat.com> 1.1.9-1
- Translation updates
- pygtk deprecations

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1.1.8-2
- Update the GTK+ theme icon cache on (un)install

* Fri Oct 01 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.8-1
- Indic UTF-8 locales
- Translations

* Wed Sep 29 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.7-1
- update locale-list (bug# 134034)

* Tue Sep 07 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.6-2
- Buildrequires intltool

* Tue Sep 07 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.6-1
- Translatable desktop

* Mon Sep 06 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.5-3
- fix gtk.mainloop/mainquit 

* Thu Apr  8 2004 Brent Fox <bfox@redhat.com> 1.1.5-2
- fix icon path (bug #120177)

* Mon Jan 12 2004 Brent Fox <bfox@redhat.com> 1.1.5-1
- update locale-list (bug #107450)

* Fri Jan  9 2004 Brent Fox <bfox@redhat.com> 1.1.4-1
- enable TUI mode

* Wed Jan 07 2004 Than Ngo <than@redhat.com> 1.1.3-1
- make changes for Python2.3

* Thu Nov 20 2003 Brent Fox <bfox@redhat.com> 1.1.2-1
- fix typo in the Obsoletes

* Wed Nov 19 2003 Brent Fox <bfox@redhat.com> 1.1.1-1
- rebuild

* Wed Nov 12 2003 Brent Fox <bfox@redhat.com> 1.1.0-1
- add Obsoletes for redhat-config-language
- make changes for Python2.3

* Mon Nov 10 2003 Brent Fox <bfox@redhat.com> 1.1.0-1
- convert redhat-config-language into system-config-language

* Mon Oct 13 2003 Brent Fox <bfox@redhat.com> 1.0.16-1
- rebuild for latest translations (bug #106618)

* Mon Sep 15 2003 Brent Fox <bfox@redhat.com> 1.0.15-2
- bump release num and rebuild

* Mon Sep 15 2003 Brent Fox <bfox@redhat.com> 1.0.15-1
- add Requires for rhpl (bug #104210)

* Thu Aug 14 2003 Brent Fox <bfox@redhat.com> 1.0.14-1
- tag on every release

* Wed Aug 13 2003 Brent Fox <bfox@redhat.com> 1.0.12-1
- remove python-tools dependency

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.11-2
- bump relnum and rebuild

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.11-1
- fix build problem

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.10-2
- bump relnum and rebuild

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.10-1
- change runPriority

* Thu Jul  3 2003 Brent Fox <bfox@redhat.com> 1.0.9-2
- bump relnum and rebuild

* Thu Jul  3 2003 Brent Fox <bfox@redhat.com> 1.0.9-1
- use UTF-8 in CJK locales (bug #98522)

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.0.8-2
- bump relnum and rebuild

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.0.8-1
- use rhpl translation module

* Thu Jun 26 2003 Brent Fox <bfox@redhat.com> 1.0.7-1
- make sure the config file is written before calling changeLocale()

* Thu Jun 26 2003 Brent Fox <bfox@redhat.com> 1.0.6-1
- add some hooks for firstboot so locale can change on the fly (#91984)

* Wed May 21 2003 Brent Fox <bfox@redhat.com> 1.0.5-1
- add some hacks to make simplified chinese work (bug #84772)

* Tue Feb 18 2003 Brent Fox <bfox@redhat.com> 1.0.4-1
- update locale-list (bug #84183)

* Wed Feb 12 2003 Jeremy Katz <katzj@redhat.com> 1.0.3-3
- fixes for cjk tui (#83518)

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.0.3-2
- fix a po file encoding problem.  please use utf-8 in the future

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.0.3-1
- bump and build

* Thu Jan 23 2003 Brent Fox <bfox@redhat.com> 1.0.2-2
- add Bulgarian to locale-list

* Thu Jan 23 2003 Brent Fox <bfox@redhat.com> 1.0.2-1
- update translations in desktop file

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 1.0.1-13
- fix dangling symlink that broke firstboot

* Mon Dec 16 2002 Brent Fox <bfox@redhat.com> 1.0.1-12
- fix a typo

* Mon Dec 16 2002 Brent Fox <bfox@redhat.com> 1.0.1-11
- show a warning if run in console mode (bug #78739)

* Sun Dec 15 2002 Brent Fox <bfox@redhat.com> 1.0.1-10
- strip off @euro from the supported langs (bug #77637)

* Tue Nov 12 2002 Brent Fox <bfox@redhat.com> 1.0.1-9
- pam path changes

* Tue Oct 15 2002 Brent Fox <bfox@redhat.com> 1.0.1-8
- Handle upgrading with different encodings in /etc/sysconfig/clock

* Thu Sep 19 2002 Brent Fox <bfox@redhat.com> 1.0.1-7
- Patch to desktop file from kmraas@online.no applied for [no] translation

* Tue Sep 10 2002 Bill Nottingham <notting@redhat.com> 1.0.1-6
- don't write SYSFONTACM="utf8"; switch default font to match anaconda

* Tue Sep  3 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-5
- Obsolete locale_config

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-4
- Convert to noarch

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-3
- Remove dupe for Romanian

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-2
- Only apply the changes if the user actually changed something

* Wed Aug 21 2002 Preston Brown <pbrown@localhost.localdomain> 1.0.1-1
- we were writing to the wrong gdm file...

* Fri Aug 16 2002 Brent Fox <bfox@redhat.com> 1.0-2
- pull translations into locale-list
- convert locale-list to UTF-8

* Fri Aug 16 2002 Preston Brown <pbrown@redhat.com> 1.0-1
- reset GDM config if lang changes

* Wed Aug 14 2002 Brent Fox <bfox@redhat.com> 0.9.9-8
- call destroy on window close

* Tue Aug 13 2002 Tammy Fox <tfox@redhat.com> 0.9.9-7
- better icon

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 0.9.9-6
- Fix desktop file icon path

* Mon Aug 12 2002 Brent Fox <bfox@redhat.com> 0.9.9-5
- update locale list

* Mon Aug 12 2002 Tammy Fox <tfox@redhat.com> 0.9.9-4
- Replace System with SystemSetup in desktop file categories

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.9.9-3
- fix desktop file

* Mon Aug 05 2002 Brent Fox <bfox@redhta.com> 0.9.9-1
- pull in desktop file translations

* Fri Aug 02 2002 Tammy Fox <tfox@redhat.com> 0.9.8-2
- Fix desktop file categories

* Fri Aug 02 2002 Brent Fox <bfox@redhat.com> 0.9.8-1
- Make changes for new pam timestamp policy

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-3
- fix Makefiles and spec files so that translations get installed

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-2
- update spec file for public beta 2

* Tue Jul 23 2002 Tammy Fox <tfox@redhat.com> 0.9.5-2
- Fix desktop file (bug #69475)

* Thu Jul 18 2002 Brent Fox <bfox@redhat.com> 0.9.5-1
- Update for pygtk2 API change

* Tue Jul 16 2002 Brent Fox <bfox@redhat.com> 0.9.4-2
- bump rev num and rebuild

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 0.9.3-2
- Update changelogs and rebuild

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 0.9.3-1
- Update changelogs and rebuild

* Mon Jul 01 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Bump rev number

* Mon Jul 01 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Bump rev number

* Thu Jun 27 2002 Brent Fox <bfox@redhat.com> 0.9.1-2
- Added a message dialog when applying changes

* Wed Jun 26 2002 Brent Fox <bfox@redhat.com> 0.9.1-1
- Fixed description

* Tue Jun 25 2002 Brent Fox <bfox@redhat.com> 0.9.4-5
- Create pot file

* Mon Jun 24 2002 Brent Fox <bfox@redhat.com> 0.9.4-4
- Fix spec file

* Fri Jun 21 2002 Brent Fox <bfox@redhat.com> 0.9.0-3
- Remove cancel button
- init doDebug to None

* Thu Jun 20 2002 Brent Fox <bfox@redhat.com> 0.9.0-2
- Don't pass doDebug into init
- Add snapsrc to Makefile

* Wed May 29 2002 Brent Fox <bfox@redhat.com> 0.2.0-6
- handle an existing but empty i18n file 

* Sun May 26 2002 Brent Fox <bfox@redhat.com> 0.2.0-5
- raise a RuntimeError if /etc/sysconfig/i18n file doesn't exist

* Tue May 14 2002 Brent Fox <bfox@redhat.com>
- improved check for existing i18n file
- added debug mode capability

* Tue Nov 28 2001 Brent Fox <bfox@redhat.com>
- initial coding and packaging

