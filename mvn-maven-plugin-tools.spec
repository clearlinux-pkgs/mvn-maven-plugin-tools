#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-plugin-tools
Version  : 3.5
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugin-plugin/3.4/maven-plugin-plugin-3.4.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugin-plugin/3.4/maven-plugin-plugin-3.4.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.pom
Source4  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2/maven-plugin-tools-api-3.5.2.jar
Source5  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2/maven-plugin-tools-api-3.5.2.pom
Source6  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2/maven-plugin-tools-generators-3.5.2.jar
Source7  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2/maven-plugin-tools-generators-3.5.2.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools/3.4/maven-plugin-tools-3.4.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools/3.5.2/maven-plugin-tools-3.5.2.pom
Source10  : https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/maven-plugin-tools/3.5/maven-plugin-tools-3.5.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-assembly-plugin/3.0.0/maven-assembly-plugin-3.0.0.jar
Source12  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-assembly-plugin/3.0.0/maven-assembly-plugin-3.0.0.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0/maven-checkstyle-plugin-3.0.0.jar
Source14  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0/maven-checkstyle-plugin-3.0.0.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.7.0/maven-compiler-plugin-3.7.0.jar
Source16  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.7.0/maven-compiler-plugin-3.7.0.pom
Source17  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-dependency-plugin/3.1.1/maven-dependency-plugin-3.1.1.jar
Source18  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-dependency-plugin/3.1.1/maven-dependency-plugin-3.1.1.pom
Source19  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1/maven-enforcer-plugin-1.4.1.jar
Source20  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1/maven-enforcer-plugin-1.4.1.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-install-plugin/2.5.2/maven-install-plugin-2.5.2.jar
Source22  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-install-plugin/2.5.2/maven-install-plugin-2.5.2.pom
Source23  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.1.0/maven-jar-plugin-3.1.0.jar
Source24  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.1.0/maven-jar-plugin-3.1.0.pom
Source25  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-plugins/24/maven-plugins-24.pom
Source26  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-plugins/25/maven-plugins-25.pom
Source27  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-plugins/30/maven-plugins-30.pom
Source28  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-plugins/31/maven-plugins-31.pom
Source29  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-remote-resources-plugin/1.5/maven-remote-resources-plugin-1.5.jar
Source30  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-remote-resources-plugin/1.5/maven-remote-resources-plugin-1.5.pom
Source31  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.jar
Source32  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.pom
Source33  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-site-plugin/3.7.1/maven-site-plugin-3.7.1.jar
Source34  : https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-site-plugin/3.7.1/maven-site-plugin-3.7.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-plugin-tools-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-plugin-tools package.
Group: Data

%description data
data components for the mvn-maven-plugin-tools package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.4
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5.2
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/24
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/24

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/25
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/25

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/30
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/30

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/31
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/31

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1
cp %{SOURCE33} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1
cp %{SOURCE34} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.jar
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-annotations/3.5/maven-plugin-annotations-3.5.pom
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2/maven-plugin-tools-api-3.5.2.jar
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-api/3.5.2/maven-plugin-tools-api-3.5.2.pom
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2/maven-plugin-tools-generators-3.5.2.jar
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools-generators/3.5.2/maven-plugin-tools-generators-3.5.2.pom
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.4/maven-plugin-tools-3.4.pom
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5.2/maven-plugin-tools-3.5.2.pom
/usr/share/java/.m2/repository/org/apache/maven/plugin-tools/maven-plugin-tools/3.5/maven-plugin-tools-3.5.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0/maven-assembly-plugin-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-assembly-plugin/3.0.0/maven-assembly-plugin-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0/maven-checkstyle-plugin-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-checkstyle-plugin/3.0.0/maven-checkstyle-plugin-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0/maven-compiler-plugin-3.7.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-compiler-plugin/3.7.0/maven-compiler-plugin-3.7.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1/maven-dependency-plugin-3.1.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-dependency-plugin/3.1.1/maven-dependency-plugin-3.1.1.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1/maven-enforcer-plugin-1.4.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-enforcer-plugin/1.4.1/maven-enforcer-plugin-1.4.1.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2/maven-install-plugin-2.5.2.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-install-plugin/2.5.2/maven-install-plugin-2.5.2.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0/maven-jar-plugin-3.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-jar-plugin/3.1.0/maven-jar-plugin-3.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4/maven-plugin-plugin-3.4.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugin-plugin/3.4/maven-plugin-plugin-3.4.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/24/maven-plugins-24.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/25/maven-plugins-25.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/30/maven-plugins-30.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-plugins/31/maven-plugins-31.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5/maven-remote-resources-plugin-1.5.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-remote-resources-plugin/1.5/maven-remote-resources-plugin-1.5.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-resources-plugin/3.1.0/maven-resources-plugin-3.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1/maven-site-plugin-3.7.1.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-site-plugin/3.7.1/maven-site-plugin-3.7.1.pom
