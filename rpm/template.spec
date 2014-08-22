Name:           ros-indigo-turtlebot-arm-ikfast-plugin
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS turtlebot_arm_ikfast_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_arm_ikfast_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
The turtlebot_arm_ikfast_plugin package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 22 2014 Jorge Santos <jsantossimon@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

* Sun Aug 17 2014 Jorge Santos <jsantossimon@gmail.com> - 0.3.0-2
- Autogenerated by Bloom

* Sat Aug 16 2014 Jorge Santos <jsantossimon@gmail.com> - 0.3.0-1
- Autogenerated by Bloom

* Sat Aug 16 2014 Jorge Santos <jsantossimon@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

