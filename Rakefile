VENV_DIR = '.venv'


def vsh *args, **kwargs
  sh([". #{VENV_DIR}/bin/activate &&", *args.map{ |x| x.to_s }].join(' '),
     **kwargs)
end


task :test do
  sh "python3 -m venv #{VENV_DIR}" unless File.directory? VENV_DIR
  vsh 'python3 setup.py install'

  Dir.glob('test/*.py').each do |file|
    vsh "python3 #{file} -h"
  end

  vsh 'python3 test/default.py'
  vsh 'python3 test/overwrite.py foo'
  vsh 'python3 test/simple.py foo'
end


task :upload => %i(clean test) do
  sh 'python3 setup.py sdist bdist_wheel'
  sh 'twine upload dist/*'
end


task :clean do
  sh 'git clean -dfx'
end
