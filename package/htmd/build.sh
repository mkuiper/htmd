echo "building"

export PATH=$PATH:/usr/bin/:/bin/
printenv

# Compile any C code


T="$PWD"
for S in "$PWD/C/"*; do
	cd "$S"
	make CC=$CC FC=$FC STATIC=$STATIC
	cd "$T"
done

find htmd -type d -name __pycache__ -exec rm -rf {} \; -print || true

echo "Installing into $PREFIX"

	DIR="$SP_DIR"

	if [ "$DIR" != "" ]; then
		mkdir -p "$DIR"
	fi
	if [ -e "$DIR" ]; then
		pwd
		ls
		cp -r htmd  $DIR/
		cp -r htmdx  $DIR/
		rm -rf $(find "$DIR" -name .git -type d) 
    rm -rf $DIR/htmd/data
	  rm -rf $DIR/htmd/.idea
	  rm -rf $DIR/htmdx/.idea
    rm -rf $DIR/htmd/.ipynb_checkpoints
    rm -rf $DIR/htmd/Untitled*
    if [ "$TYPE" == "basic" ]; then
      rm -rf $DIR/htmd/lib/pro
		fi
    if [ "$TYPE" == "pro" ]; then
      rm -rf $DIR/htmd/lib/basic
		fi


    echo "def version():" > $DIR/htmd/version.py
    echo "    return \"$PKG_VERSION\"" >> $DIR/htmd/version.py

	else
		echo "Error: SP_DIR not defined"
		exit 1
	fi

cd "$SP_DIR/../../"

chmod -R a+rX "$PREFIX"


#for T in 3.4 3.5; do
#	if [ "$T" != "$PY_VER" ]; then
#		mkdir -p python${T}/site-packages
#		cd python${T}/site-packages
#		ln -s ../../python${PY_VER}/site-packages/htmd .
#		ln -s ../../python${PY_VER}/site-packages/htmdx .
#	cd -
#	fi
#done

exit 0
