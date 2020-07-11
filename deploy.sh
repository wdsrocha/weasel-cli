version=`echo $(poetry version) | awk '{print $NF}'`

has_unstaged_version_change=`git diff pyproject.toml | grep +version`
has_staged_version_change=`git diff --cached pyproject.toml | grep +version`

if [[ "$has_unstaged_version_change" != "" || "$has_staged_version_change" != "" ]]; then
    echo "error: project version does not match the version from current commit."
    echo "did you forgot to commit the pyproject.toml changes?"
    exit 1
fi

while true; do
    echo "this command will create and push the v${version} tag to master."
    read -p "are you sure you wish to proceed? [y/N] " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit 0;;
        * ) echo "Please answer yes or no.";;
    esac
done

git tag "v${version}"

echo "pushing tag to master..."
git push origin master --tags && echo "done."
