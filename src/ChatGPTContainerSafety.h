#pragma once
#import <Foundation/Foundation.h>

// Rootful system applications can be misregistered with a shared HOME.
// Never allow custom profile seeding or recursive cleanup in that case.
static inline NSString *CGPrivateAppContainer(void) {
    NSString *home = NSHomeDirectory().stringByResolvingSymlinksInPath;
    NSString *a = @"/private/var/mobile/Containers/Data/Application/";
    NSString *b = @"/var/mobile/Containers/Data/Application/";
    NSString *prefix = [home hasPrefix:a] ? a : ([home hasPrefix:b] ? b : nil);
    if (!prefix) return nil;
    NSString *uuid = [home substringFromIndex:prefix.length];
    if (![[NSUUID alloc] initWithUUIDString:uuid]) return nil;
    NSString *metadataPath = [home stringByAppendingPathComponent:@".com.apple.mobile_container_manager.metadata.plist"];
    NSDictionary *metadata = [NSDictionary dictionaryWithContentsOfFile:metadataPath];
    NSString *identifier = metadata[@"MCMMetadataIdentifier"];
    if (identifier && ![identifier isEqualToString:NSBundle.mainBundle.bundleIdentifier]) return nil;
    return home;
}
static inline BOOL CGHasPrivateAppContainer(void) {
    return CGPrivateAppContainer() != nil;
}
static inline BOOL CGPathIsWithinAppContainer(NSString *path) {
    NSString *home = CGPrivateAppContainer();
    if (!home.length || !path.length) return NO;
    NSString *resolved = path.stringByResolvingSymlinksInPath;
    return [resolved hasPrefix:[home stringByAppendingString:@"/"]];
}
