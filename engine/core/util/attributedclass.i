%module util 
%{
#include "util/attributedclass.h"
#include "util/point.h"
#include "util/rect.h"
%}

%include "util/point.i"
%include "util/rect.h"

namespace FIFE {

	class AttributedClass {
		public:

			AttributedClass(const std::string& identifier);
			~AttributedClass();

			const std::string& Id() const;

			std::vector<std::string> listFields() const;
			const std::string& get(const std::string& field);
			void set(const std::string& field, const std::string& value);
			void remove(const std::string& field);

		private:
	};
}
