task :test do
  Dir.glob('test/*.py').each do |file|
    sh 'python3', file, '-h'
  end
end


task :upload => %i(clean test) do
  sh 'python3 setup.py sdist bdist_wheel'
  sh 'twine upload dist/*'
end


task :clean do
  sh 'git clean -dfx'
end
