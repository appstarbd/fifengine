%module model
%{
#include "model/structures/layer.h"
%}

%include "std_vector.i"

%include "util/point.h"
%include "util/attributedclass.i"

namespace FIFE { namespace model {
  class Instance;
} }

namespace std {
  %template(InstanceVector) vector<FIFE::model::Instance*>;
}

namespace FIFE { namespace model {

	class Elevation;
	class Selection;
	class Instance;
	class Object;

	class Layer : public AttributedClass {
		public:
			Layer(Elevation* elevation, CellGrid* geometry);
			~Layer();

			Elevation* getElevation();
			bool hasInstances() const;
			Instance* addInstance(Object* object, const Point& p);
			void removeInstance(Instance* object);
			const std::vector<Instance*>& getInstances();

			template<typename T>
			std::vector<Instance*> getInstances(const std::string& field, const T& value);
			%template(getInstancesByBool) getInstances<bool>;
			%template(getInstancesByInt) getInstances<long>;
			%template(getInstancesByRect) getInstances<Rect>;
			%template(getInstancesByPoint) getInstances<Point>;
			%template(getInstancesByString) getInstances<std::string>;

			void setInstancesVisible(bool vis);
			void toggleInstancesVisible();
			bool areInstancesVisible() const;

			void update();
	};
}}
