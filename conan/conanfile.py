from conans import ConanFile, CMake, tools

class ScmtestConan(ConanFile):
    name = "conan-test"
    version = "0.0.0"
    url = ""
    description = "Try the optional setting cppstd"
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    exports_sources = "main.cpp"


    def build(self):
        print("The cpp standard is: {}".format(self.settings.cppstd))
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        # Done by the install step in build()
        pass

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
