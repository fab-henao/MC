import setuptools

setuptools.setup(
    name='MC',
    version='0.0.1',
    author='Fabian Henao',
    description='Es un paquete que te permitira obtener datos de un usuario de Minecraft y de los Servicios de Mojan y servidores de Minecraft',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    author_mail='fabianfeik474@gmail.com',
    url='https://github.com/fab-henao/MC.git',
    keywords=["mojang", "minecraft", "api", "mojang api", "minecraft api"]
)