.PHONY: all install clean

all:
	@echo "🔥 Building ShadowDaemon Ultimate..."
	pip install -r requirements.txt
	$(MAKE) -C kernel
	@echo "✅ Build complete!"

install:
	@echo "🚀 Installing ShadowDaemon..."
	mkdir -p /opt/shadow
	cp -r . /opt/shadow/
	cd /opt/shadow && python3 shadow.py &
	@echo "✅ ShadowDaemon running!"

clean:
	rm -rf __pycache__ *.pyc
	rm -rf /tmp/*shadow*
	@echo "🧹 Cleaned up!"